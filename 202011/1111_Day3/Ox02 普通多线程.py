# -*- coding: utf-8 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201113 -*-
from time import sleep
import time
import threading


def f1():
	print('f1', time.time())
	sleep(1)
	pass


def f2():
	print('f2', time.time())
	sleep(1)
	pass


if __name__ == '__main__':
	gThread = [threading.Thread(target=f1), threading.Thread(target=f2)]
	for th in gThread:
		th.start()
	for th in gThread:
		if th.is_alive():
			th.join()
	pass
