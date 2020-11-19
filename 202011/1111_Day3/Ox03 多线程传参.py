# -*- coding: utf-8 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201113 -*-
from time import sleep
import threading


def f1(thid, imax):
	print('>线程传入的参数', thid, imax)
	for i in range(imax):
		print(f'>>线程{thid}', f'计数{i + 1}/{imax}')
		sleep(0.01)
	print('>线程%d 退出' % thid)
	pass


def f2(i):
	__th = threading.Thread(target=f1, args=(i + 1, 5))
	__th.start()
	return __th


if __name__ == '__main__':
	gThreadN = 2
	gThreads = list(map(f2, range(gThreadN)))
	print(gThreads)
	for th in gThreads:
		if th.is_alive():
			th.join()
	pass
