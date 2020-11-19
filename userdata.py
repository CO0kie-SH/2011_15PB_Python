# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201118 -*-


"""↓↓↓用户编辑参数段↓↓↓"""
Global_UserData = {
    'Thread-Num': 1,
    'XlsSavePath': 'E:\\',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
"""↑↑↑用户编辑参数段↑↑↑"""

# 初始化注入参数
Global_UserData['inj_type'] = ['1', "1'", "1')", "1'))", '1"', '1")', '1"))']
Global_UserData['inj_url'] = 'http://127.0.0.1:8001/sqli/Less-{}/?id=%s'

# 初始化靶场 关卡url
Global_UserData['inj_urls'] = [Global_UserData['inj_url'].format(i + 1) for i in range(9)]
