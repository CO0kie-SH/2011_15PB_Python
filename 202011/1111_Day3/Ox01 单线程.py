# -*- coding: utf-8 -*-
# -*- coder : CO0kie丶 -*-
# -*- time  : 20201113 -*-
from time import sleep
import time


def f1():
	print('f1', time.time())
	sleep(1)
	pass


def f2():
	print('f2', time.time())
	sleep(1)
	pass


if __name__ == '__main__':
	f1()
	f2()
