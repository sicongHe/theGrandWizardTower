#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import Queue
import time
from multiprocessing.managers import BaseManager
import random
import copy
from tools import *
cardbook1 = Cardbook()
cardbook2 = Cardbook()
cardbook1.addcard(1,Mofafeidan())
cardbook1.addcard(2,Fanzhi())
cardbook1.addcard(3,Fanzhi())
cardbook1.addcard(4,Mofafeidan())
cardbook1.addcard(5,Mofafeidan())
cardbook1.addcard(6,Fanzhi())
cardbook1.addcard(7,Mayoufuweiliuxing())
cardbook1.addcard(8,Moqiuliyazhiguang())
cardbook1.addcard(9,Dabengmieshu())
cardbook1.addcard(10,Mayoufuqiangsuanjian())
cardbook1.addcard(11,Nengliangsuzao())
cardbook1.addcard(12,Nengliangsuzao())
cardbook1.addcard(13,Nengliangsuzao())
cardbook1.addcard(14,Nengliangsuzao())
cardbook1.addcard(15,Huolongjuan())
cardbook1.addcard(16,Huolongjuan())
cardbook1.addcard(17,Leitingdiyu())
cardbook1.addcard(18,Leitingdiyu())
cardbook1.addcard(19,Mingxiang())
cardbook1.addcard(0,Lunkong())

cardbook2 = copy.deepcopy(cardbook1)
tester1 = Player()
tester2 = Player()
tester1.setname('jb')
tester2.setname('jbb')
cardbook1.setowner(tester1)
cardbook2.setowner(tester2)

tester1.setcardbook(cardbook1)
tester2.setcardbook(cardbook2)


class QQueueManager(BaseManager):
	"""docstring for QueueManager"""
	pass


def onegame():	
	port = Queue.Queue()
	idq = Queue.Queue()
	recva = Queue.Queue()
	senda = Queue.Queue()
	recvb = Queue.Queue()
	sendb = Queue.Queue()
	QQueueManager.register('portqueue', callable = lambda: port)
	QQueueManager.register('idqueue', callable = lambda: idq)
	QQueueManager.register('ats', callable = lambda: recva)
	QQueueManager.register('bts', callable = lambda:recvb)
	QQueueManager.register('sta', callable = lambda:senda)
	QQueueManager.register('stb', callable = lambda:sendb)
	manager = QQueueManager(address = ('', 6000), authkey = 'llbza')
	manager.start()
	print '总服务器已经开启'
	port_queue = manager.portqueue()
	id_queue = manager.idqueue()
	a_to_s = manager.ats()
	b_to_s = manager.bts()
	s_to_a = manager.sta()
	s_to_b = manager.stb()
	port_queue.put(6666)
	port_queue.put(6666)
	id_queue.put('A')
	id_queue.put('B')
	#在id队列中放入AB 由客户端去接收
	a_name = a_to_s.get().encode('utf8')
	b_name = b_to_s.get().encode('utf8')
	if a_name == 'jb':
		A = tester1
	if b_name == 'jb':
		B = tester1
	if a_name == 'jbb':
		A = tester2
	if b_name == 'jbb':
		B = tester2
	print '两位玩家已经就位'
	s_to_a.put('*战斗端口分配中*')
	s_to_b.put('*战斗端口分配中*')
	game = Game(A, B, 6666)
	return game

def gamestart(game):
	game.gamestart()

gamestart(onegame())


