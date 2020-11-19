# -*- coding: utf-8 -*-
# -*- ver	: >3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201116 -*-

import urllib.request
import urllib.parse


# noinspection PyPep8Naming
class CUrllib(object):
    def __init__(self, Url: str, Mode='GET', Data=None, Cookie: str = ""):
        # self.headers = {}
        self.url = Url
        self.request = None
        self.data = None
        if Mode == "GET":
            self.request = urllib.request.Request(Url)
        elif Mode == 'POST':
            _data = None
            if type(Data) == dict:
                _data = bytes(urllib.parse.urlencode(Data), encoding='utf8')
            # print('编码后', _data)
            elif type(Data) == str:
                _data = Data.encode()
            else:
                print('err:POST_DATA')
                exit(8)
            self.request = urllib.request.Request(Url, data=_data)
            self.request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
        else:
            print('HTTP请求输入了错误参数')
            exit(9)
        if Cookie != "":
            self.request.add_header("Cookie", Cookie)
        self.content = None
        pass

    def Send(self):
        self.content = urllib.request.urlopen(self.request)
        pass

    def GetMessage(self):
        print(self.content.getcode(), self.content.geturl())
        print(self.content.getheaders())
        self.data = self.content.read()
        pass

    pass


if __name__ == '__main__':
    gUrl = r'http://httpbin.org/get'

    http = CUrllib(gUrl)
    http.Send()
    http.GetMessage()
    print(http.data.decode())
    data = {'word': 'hello'}
    http = CUrllib(r'http://127.0.0.1:8000/test.php', "POST", data)
    http.Send()
    http.GetMessage()
    print(http.data.decode())
    pass
