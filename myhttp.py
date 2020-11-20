# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201119 -*-
import requests
import re
from time import perf_counter


class HTTP(object):
    content = None
    con_len = 0
    old_time = 0.0
    new_time = 0.0

    def GetSelf(self):
        return self

    def RefNewTime(self):
        self.old_time = self.new_time
        self.new_time = perf_counter()
        pass

    def GET(self, Url: str, Lock=None):
        """
        函数：GET请求

        :param Url: URL统一资源定位器
        :param Lock: 线程锁，传入时会打印过程
        :return: 响应体长度
        """
        self.content = requests.get(Url)
        self.old_time = self.new_time
        self.new_time = perf_counter()
        self.con_len = int(self.content.headers['Content-Length']) \
            if 'Content-Length' in self.content.headers \
            else int(len(self.content.content))
        if Lock is not None:
            Lock.acquire()
            print(f'>>HTTP_GET {self.content.status_code} '
                  f'Len={self.con_len} newTime={self.new_time} '
                  f'【{Url}】')
            Lock.release()
        return self.con_len, self.content.status_code,

    def GET_RE(self, Url: str, Code: str, Re: str, Lock=None):
        """
        函数：Get请求，且使用re过滤字符串

        :param Url: 注入URL
        :param Code: 注入语句
        :param Re: 正则匹配规则
        :param Lock: 默认为空：线程锁，传入时会打印结果
        :return: 成功返回[字符串列表],失败返回None
        """

        newlen, code = self.GET(Url % Code)
        if Lock is not None:
            Lock.acquire()
            print(f'>>>>{code=},{newlen=}【{Url % Code}】')
            print(self.content.text.replace('\r\n', ''))
            Lock.release()

        find_list = re.findall(Re, self.content.text)
        # print(f'{Re=}', len(find_list), find_list)
        if len(find_list) > 0:
            ret_data = find_list[0]
            return int(ret_data) if ret_data.isdigit() else ret_data
        return None
        pass

    pass
