# -*- coding: utf-8 -*-
# -*- ver	: >3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201116 -*-

# noinspection PyUnresolvedReferences
import urllib3
import re
from bs4 import BeautifulSoup


class DangDang(object):
    def __init__(self):
        self.Url = 'http://search.dangdang.com/?key=JAVA'
        self.http = urllib3.PoolManager()
        self.response = None
        pass

    def SendHttp(self):
        self.response = self.http.request("GET", self.Url)
        pass

    def CheckBody3(self):
        print('`' * 22, self.response.status)

        # 创建一个基于内置解析器的 bs 对象，用于分析 html 网页
        soup = BeautifulSoup(self.response.data.decode('GBK'), 'html.parser')

        # 直接传入一个参数，表示查找到的是标签
        lvs = [['标题', '热度', '标记', '链接']]
        for index, item in enumerate(soup.find_all(class_='bigimg')[0]):
            if len(item) == 1:
                continue
            print(list(item))
            for index2, item2 in enumerate(item):
                if index2 == 0:
                    continue
                print('\t', index2, item2)
                if index2 == 1:
                    print('书名\t', item2['title'].strip())
                    print('封面\t', item2.img['src'].strip())
                elif index2 == 2:
                    print('说明\t', item2.a['title'].strip())
                    print('链接\t', item2.a['href'].strip())
                elif index2 == 3:
                    print('介绍\t', item2.text.strip())
                elif index2 == 4:
                    for prices in item2.select('span'):
                        print('价格\t', prices.text.strip())
                elif index2 == 6:
                    print('评论\t', item2.a.text.strip())
                elif index2 == 7:
                    print('作者\t', item2.a.text.strip())
            exit(1)
        pass

    pass


if __name__ == '__main__':
    dangdang = DangDang()
    dangdang.SendHttp()
    dangdang.CheckBody3()
