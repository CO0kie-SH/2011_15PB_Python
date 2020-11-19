# -*- coding: utf-8 -*-
# -*- ver	: >3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201116 -*-

import urllib3
import json


# noinspection PyPep8Naming
class CUrllib3(object):
    def __init__(self, Cookie: str = ""):
        self.Cookie = Cookie

        # 创建PoolManager对象生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
        self.http = urllib3.PoolManager()
        self.response = None
        self.Code = 0
        pass

    def Send(self, Url: str, Mode: str = 'GET', Data=None):
        self.Code = 0
        if Mode == 'GET':
            self.response = self.http.request(Mode, Url)
        elif Mode == 'POST':
            self.response = self.http.request(Mode, Url, fields=Data)
            pass
        else:
            print('HTTP_MODE ERROR')
            exit(9)
        self.Code = self.response.status
        pass

    def GetMessage(self):
        print(self.response.status)
        print(self.response.data.decode('utf-8'))
        pass

    pass


if __name__ == '__main__':
    gUrl = r'http://httpbin.org/get'
    gUrlP = r'http://httpbin.org/post'

    http = CUrllib3()
    http.Send(gUrl)
    http.GetMessage()
    data = {'word': 'hello'}
    http.Send(gUrlP, 'POST', data)
    http.GetMessage()
    pass
