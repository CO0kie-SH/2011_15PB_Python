# -*- coding: utf-8 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201113 -*-
import threading
from time import sleep


class MyThread(threading.Thread):
	def __init__(self, lock, thid):
		threading.Thread.__init__(self)
		self.lock = lock
		self.thid = thid
		self.start()

	def print(self, text: str):
		self.lock.acquire()
		print(f'>>{self.name}：{text}')
		self.lock.release()

	def run(self):
		global num
		self.print(f'传入 {self.name} {num}')
		for i in range(num):
			self.print(f'计数{i + 1}/{num}')
			sleep(0.01)
		self.print('退出')


class ThreadCtrl(object):
	def funinit(self, thid):
		return MyThread(self.lock, thid + 1)

	def __init__(self, threadNum: int):
		self.lock = threading.Lock()
		self.Threads = list(map(self.funinit, range(threadNum)))
		pass


if __name__ == '__main__':
	num = 5
	ThreadCtrl(2)
