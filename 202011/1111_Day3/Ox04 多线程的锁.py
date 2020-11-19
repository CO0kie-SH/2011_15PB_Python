# -*- coding: utf-8 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201113 -*-
from time import sleep
import threading


def f1(lock, thid, imax):
	lock.acquire()
	print('>线程传入的参数', thid, imax)
	lock.release()
	for i in range(imax):
		lock.acquire()
		print(f'>>线程{thid} 计数{i + 1}/{imax}')
		lock.release()
		sleep(0.01)
	lock.acquire()
	print('>线程%d 退出' % thid)
	lock.release()
	pass


def f2(i):
	global gThLock
	__th = threading.Thread(target=f1, args=(gThLock, i + 1, 5))
	__th.start()
	return __th


if __name__ == '__main__':
	gThLock = threading.Lock()
	gThreadN = 2
	gThreads = list(map(f2, range(gThreadN)))
	for th in gThreads:
		if th.is_alive():
			th.join()
	pass
