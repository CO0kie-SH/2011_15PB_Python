# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201119 -*-
import pprint
from openpyxl import Workbook

pp = pprint.PrettyPrinter()


def SaveXlsx2(Path: str, Dict):
    for url in Dict:
        print(f'\n【{url}】')
        pp.pprint(Dict[url])
    pass


# noinspection PyBroadException
def SaveXlsx(FileName: str, Dict):
    """
    函数： 保存Dict里的值

    :param FileName: 文件路径
    :param Dict: 传入的漏洞信息
    :return: T/F=是否保存成功
    """

    # 保存xlsx
    wb = Workbook(write_only=True)

    ws1 = wb.create_sheet('数据库信息')

    for data in Dict:
        if '注入方式' == data:
            continue

        # 排版信息
        if '脱裤_数据库信息' == data:
            for data2 in Dict[data]:
                ws1.append((data2, Dict[data][data2]))
        elif '脱裤_数据库数据' == data:
            for tb_name in Dict[data]:
                ws = wb.create_sheet(tb_name)
                for line in Dict[data][tb_name]['data']:
                    ws.append(line)
                ws.close()
        elif '注入' in data:
            ws1.append((data, Dict[data]))
            pass

    # print(Dict)
    print(FileName)
    wb.save(FileName)
    wb.close()
    pass
