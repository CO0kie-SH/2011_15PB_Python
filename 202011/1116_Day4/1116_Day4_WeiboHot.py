# -*- coding: utf-8 -*-
# -*- ver	: >3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201116 -*-

# noinspection PyUnresolvedReferences
import urllib3
import re
from bs4 import BeautifulSoup


class WeiboHot(object):
    def __init__(self):
        self.Url = 'https://s.weibo.com/top/summary'
        self.http = urllib3.PoolManager()
        self.response = None
        pass

    def SendHttp(self):
        self.response = self.http.request("GET", self.Url)
        pass

    def CheckBody1(self):
        print(self.response.status)
        # print(self.response.data.decode('utf-8'))

        # 得到Body字符串、并初始化字符串参数
        _body = self.response.data.decode('utf-8') \
            .replace(' ', '') \
            .replace('\n', '')
        _left, _rig = 0, _body.find('</tr>')

        # 循环提取字符串，热搜固定数量51，所以直接用for
        for i in range(51):
            _left = _body.find('<tr', _rig)
            _rig = _body.find('</tr>', _left)
            # print(_left, _rig, _body[_left:_rig])

            # 分别提取各个td的信息
            # 提取链接
            _left = _body.find('<ahref="', _left, _rig) + 8
            # print('\t' + _body[_left:_body.find('"t', _left)])
            # 提取标题
            _left = _body.find('>', _left, _rig) + 1
            print(f'\t{i}\t标题[' + _body[_left:_body.find('<', _left)], end=']\t')
            # 提取热度
            _left = _body.find('n>', _left, _rig) + 2
            print('\t热度[' + _body[_left:_body.find('<', _left)], end=']')
            # 提取标记
            _left = _body.rfind('</i>', _left, _rig)
            if _left > 0:
                print(f'【{_body[_body.rfind(">", 0, _left) + 1:_left]}】')
            else:
                print()
        pass

    def CheckBody2(self):
        print(self.response.status)
        # print(self.response.data.decode('utf-8'))

        # 得到Body字符串、并初始化字符串参数
        _body = self.response.data.decode('utf-8') \
            .replace(' ', '') \
            .replace('\n', '')
        find_list = re.findall(r'<trclass="">.+?weibo.+?".+?">'
                               r'(.+?)</a>.+?(\d+)'
                               r'(.+?)([</i>]{0,4})</td></tr>', _body)
        for index, x in enumerate(find_list):
            print(index, x)
        pass

    def CheckBody3(self):
        print('`' * 22, self.response.status)

        # 创建一个基于内置解析器的 bs 对象，用于分析 html 网页
        soup = BeautifulSoup(self.response.data, 'html.parser')

        # 直接传入一个参数，表示查找到的是标签
        lvs = [['标题', '热度', '标记', '链接']]
        for index, item in enumerate(soup.find_all('tr')[1:]):
            lv = ['', None, None]
            # print(index, len(item), list(item))
            link = item.select('.td-02 a')
            lv[0] = link[0].text
            for x in item.select('.td-02 span'):
                lv[1] = int(x.text)
            for x in item.select('.td-03 i'):
                lv[2] = x.text
            lv.append(link[0]['href'])
            print(lv)
            lvs.append(lv)
        print('·' * 22)
        pass

    pass


if __name__ == '__main__':
    weibo = WeiboHot()
    weibo.SendHttp()
    # weibo.CheckBody1()
    # weibo.CheckBody2()
    weibo.CheckBody3()
