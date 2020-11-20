# -*- coding: utf-8 -*-
# -*- ver	: >=3.8.0 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201118 -*-


import threading
import queue
from time import sleep
from userdata import Global_UserData
from Scanner import UrlInjector
from savedata_xlsx import SaveXlsx2


# # 初始化全局函数
# GetResult_ERROR = inj_exp.GetResult_ERROR
# SelectTables = inj_exp.SelectTables

# 初始化全局参数
# Global_UserData = userdata.Global_UserData
# Global_XlsSavePath = Global_UserData['XlsSavePath']
# Global_Headers = {'User-Agent': Global_UserData['User-Agent']}


class MyThread(threading.Thread):
    def __init__(self, _lock, _thid, _que):
        threading.Thread.__init__(self)
        self.lock = _lock
        self.thid = _thid
        self.que = _que
        self.max = _que.qsize()

    def print(self, text: str):
        self.lock.acquire()
        print(f'>>{self.name}：{text}')
        self.lock.release()

    def run(self):
        self.print(f'线程启动 {self.thid};队列数 {self.max}')
        # sleep(0.01)
        while not self.que.empty():
            task = self.que.get()
            sleep(0.05)
            self.print(f'得到队列\t{task}\t/{self.max}')
            UrlInjector(self.lock, self.name, task)
            # sleep(0.01)
        self.print('退出')


class ThreadCtrl(object):
    def funinit(self, thid):
        return MyThread(self.lock, thid + 1, self.que)

    def __init__(self, _threadNum, _que):
        self.que = _que
        self.lock = threading.Lock()
        self.Threads = list(map(self.funinit, range(_threadNum)))

    def start(self, _bJoin=True):
        # 循环启动线程
        for th in self.Threads:
            th.start()

        # 循环等待线程返回
        if not _bJoin:
            return
        for th in self.Threads:
            if th.is_alive():
                th.join()
        return


if __name__ == '__main__':
    # 初始化队列
    que = queue.Queue()
    # 循环加入队列
    for url in Global_UserData['inj_urls']:
        que.put(url)
    # que.put()

    # 初始化线程，并启动
    ThreadCtrl(
        Global_UserData['ThreadNum'],
        que).start(True)

    print('>主线程开始输出结果')
    if len(Global_UserData['result']) > 0:
        SaveXlsx2(Global_UserData['XlsSavePath'], Global_UserData['result'])
    print('>主线程结束')
    pass
