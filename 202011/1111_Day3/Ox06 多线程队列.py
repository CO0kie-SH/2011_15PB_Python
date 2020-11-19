# -*- coding: utf-8 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201113 -*-
import threading
import queue
from time import sleep
from functools import reduce


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
		self.print(f'传入 {self.thid};队列数 {self.max}')
		sleep(0.01)
		while not self.que.empty():
			task = self.que.get()
			self.print(f'计数{task}/{self.max}')
			sleep(0.01)
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
	for i in range(10):
		que.put(i + 1)
	# 初始化线程，并启动
	ThreadCtrl(2, que).start(True)
	print('>主线程结束')
	pass
