# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201118 -*-

import sys
from time import sleep

import requests

from userdata import Global_UserData
from myhttp import HTTP
from inj_union import InjUnion
from inj_err import InjError
from inj_time import InjTime

print('我被打印了_Inj_SQLite.py')

# 初始化全局参数
Global_Headers = {'User-Agent': Global_UserData['User-Agent']}


class SqlLiteInjector(HTTP):
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
        self.Print('联系作者更新，SQLite第38行')
        return False
        pass

    def __init__(self, Lock, ThreadName, Url):
        """
        构造函数：初始化扫描器类

        :param Lock: 传入的线程锁
        :param ThreadName: 传入的线程名
        :param Url: 传入的Url
        """
        super().__init__(Global_Headers)
        self._lock = Lock
        self._threadname = ThreadName
        self._url = Url

        self.Print(f'扫描器传入 {Url=}')

        try:
            self.body_len, code = self.GET(Url % '1')
            self.Print(f'初始化Len {self.body_len}')
        except requests.exceptions.ConnectionError as e:
            self.Print(f'ERROR 请检查链接 {e}')
            pass
        if not self.body_len > 0:
            self.Print(f'无法注入，请检查该网页是否正常【{Url % "1"}】')
            return
        self._inj_info = {}

        # 初始化参数完毕，开始检测注入点
        if self.CheckInj():
            # 保存结果
            self._lock.acquire()
            # print(f">>>>{self._threadname}：", self._url, self._inj_info)
            Global_UserData['result'][self._url] = self._inj_info.copy()
            self._lock.release()
        pass

    pass
