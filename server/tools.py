#!/usr/bin/env python
# -*- coding:utf-8 -*-
from card import *
from race import *
from cardbook import *
from player import *
import copy
import Queue
from multiprocessing.managers import BaseManager
import sys
import time
import random
class Portmanager(object):
	"""docstring for Portmanager"""
	def __init__(self):
		super(Portmanager, self).__init__()
		self.portlist = []

class QueueManager(BaseManager):
	"""docstring for QueueManager"""
	pass
		

# class Eventlist(object):
# 	"""事件通知表超类"""
# 	def __init__(self):
# 		self.listeners = []
# 		self.events = []
# 	def addlistener(self,card):
# 		self.listeners.append(card)
# 		print '加入监听者 ' + card.name
# 		print '监听表长度:'
# 		print len(self.listeners)
# 		print '事件表长度:'
# 		print len(self.events)
# 	def poplistener(self,card):
# 		self.listeners.remove(card)
# 	def addevent(self,event):
# 		self.events.append(event)
# 		print '加入事件 ' + event.name
# 		print '事件表长度:'
# 		print len(self.events)
# 		print '监听表长度:'
# 		print len(self.listeners)
# 	def popevent(self,event):
# 		print '正在抛出...'
# 		self.events.remove(event)
# 		print '抛出一个反制事件后的事件表长度'
# 		print len(self.events)
# 	def notify(self):
# 		print self.name + '表'
# 		print '监听表长度:'
# 		print len(self.listeners)
# 		print '事件表长度:'
# 		print len(self.events)
# 		print '监听者列表正在通知:'
# 		for i in self.listeners:
# 			print i.name
# 			i.update()
# 		print '事件列表正在通知'
# 		for i in self.events:
# 			print i.name
# 			i.update()


class Eventlist(object):
	"""docstring for Counterspell"""
	
	def __init__(self, name):
		self.name = name
		self.listeners = []
		self.events = []
	def addlistener(self,card):
		self.listeners.append(card)
		print '加入监听者 ' + card.name
		print '监听表长度:'
		print len(self.listeners)
		print '事件表长度:'
		print len(self.events)
	def poplistener(self,card):
		self.listeners.remove(card)
	def addevent(self,event):
		self.events.append(event)
		print '加入事件 ' + event.name
		print '事件表长度:'
		print len(self.events)
		print '监听表长度:'
		print len(self.listeners)
	def popevent(self,event):
		print '正在抛出...'
		self.events.remove(event)
		print '抛出一个反制事件后的事件表长度'
		print len(self.events)
	def notify(self):
		print self.name + '表'
		print '监听表长度:'
		print len(self.listeners)
		print '事件表长度:'
		print len(self.events)
		print '监听者列表正在通知:'
		if len(self.listeners) != 0 :
			for i in self.listeners:
				if i.useful == True:
					print i.name
					i.update()
		print '事件列表正在通知:'
		if len(self.events) != 0:
			for i in self.events:
				if i.useful == True:
					print i.name
					i.update()
	def timewalk(self):
		if len(self.listeners) != 0:
			for i in self.listeners:
				if i.useful == True:
					i.timeout -= 1
		if len(self.events) != 0:
			for i in self.events:
				if i.useful == True:
					i.timeout -= 1
		print '进行列表的时间操作'
























class Game(object):
	"""每一局游戏都是一个类"""
	def __init__(self, player_a, player_b, port):
		super(Game, self).__init__()
		self.player_a = player_a
		self.player_b = player_b
		self.port = port
		self.send_to_A = Queue.Queue()
		self.send_to_B = Queue.Queue()
		self.a_send_to_server = Queue.Queue()
		self.b_send_to_server = Queue.Queue()
		self.lists = []
	def startserver(self):
		QueueManager.register('sta', callable = lambda: self.send_to_A)
		QueueManager.register('stb', callable = lambda: self.send_to_B)
		QueueManager.register('ats', callable = lambda: self.a_send_to_server)
		QueueManager.register('bts', callable = lambda: self.b_send_to_server)
		print '游戏服务器即将开启于端口 ' + str(self.port)
		self.manager = QueueManager(address = ('', self.port), authkey = 'llvza')
		self.manager.start()
		print '游戏服务器开启'
		self.s_t_a = self.manager.sta()
		self.s_t_b = self.manager.stb()
		self.a_t_s = self.manager.ats()
		self.b_t_s = self.manager.bts()
		
	def endserver(self):
		self.manager.shutdown()

	def sendtoa(self, something):
		self.s_t_a.put(something)

	def sendtob(self, something):
		self.s_t_b.put(something)

	def sendtoAll(self,something):
		self.sendtoa(something)
		self.sendtob(something)

	def recvfroma(self):
		print ' 正在等待来自a的返回'
		return self.a_t_s.get().encode('utf8')

	def recvfromb(self):
		print ' 正在等待来自b的返回'
		return self.b_t_s.get().encode('utf8')

	def chushihua(self):
		self.counterspelllist = Eventlist('Counterspell')
		self.lists.append(self.counterspelllist)

	def update(self):
		for i in self.lists:
			i.notify()
	def timewalk(self):
		for i in self.lists:
			i.timewalk()

	def statereturn(self, tmpplayer):
		tmp = tmpplayer.name + '剩余血量: ' + str(tmpplayer.hp) + ' 当前防御值: ' + str(tmpplayer.defence)
		return tmp

	def bindlists(self):
		for i in self.player_a.cardbook.book:
			self.player_a.cardbook.book[i].bindlists(self.lists)
		for i in self.player_b.cardbook.book:
			self.player_b.cardbook.book[i].bindlists(self.lists)
		self.player_a.bookback = copy.deepcopy(self.player_a.cardbook)
		self.player_b.bookback = copy.deepcopy(self.player_b.cardbook)
		for i in self.player_a.bookback.book:
			self.player_a.bookback.book[i].bindlists(self.lists)
			self.player_a.bookback.book[i].owner = self.player_a.cardbook.book[i].owner
		for i in self.player_b.bookback.book:
			self.player_b.bookback.book[i].bindlists(self.lists)
			self.player_b.bookback.book[i].owner = self.player_b.cardbook.book[i].owner
		self.update()

	def oneround(self, round):
		print('通知两位玩家本回合开始 给出本回合可用的法术书')
		self.sendtoAll('回合 ' + str(round))
		self.sendtoAll('您的法术书:')

		for k in self.player_a.cardbook.book:
			self.sendtoa(str(k) + self.player_a.cardbook.book[k].name)
		for k in self.player_b.cardbook.book:
			self.sendtob(str(k) + self.player_b.cardbook.book[k].name)



		#如果本回合正在使用的法术为空 则通知玩家录入新法术
		if self.player_a.usingcard == 0:
			print '玩家A出牌'
			#每一张牌都会在打出的一瞬间执行use函数
			while self.player_a.usingcard == 0:
				self.sendtoa('-请选择法术')
				try:
					num = int(self.recvfroma())
				except BaseException,e:
					print e
					num = 0
				for i in self.player_a.cardbook.book:
					if num == i:
						self.player_a.usingcard = self.player_a.cardbook.usecard(num)
						self.player_a.usingcard.enemey = self.player_b
			print '玩家A出牌完毕'
			self.player_a.cardbook.update()

		if self.player_b.usingcard == 0:
			print '玩家B出牌'
			#每一张牌都会在打出的一瞬间执行use函数
			while self.player_b.usingcard == 0:
				self.sendtob('-请选择法术')
				try:
					num = int(self.recvfromb())
				except BaseException,e:
					print e
					num = 0
				for i in self.player_b.cardbook.book:
					if num == i:
						self.player_b.usingcard = self.player_b.cardbook.usecard(num)
						self.player_b.usingcard.enemey = self.player_a
						
			print '玩家B出牌完毕'
			self.player_b.cardbook.update()

		#测试
		#print (self.player_a.usingcard.lists == self.player_b.usingcard.lists)
		#print (self.player_a.usingcard.listenlist == self.player_b.usingcard.eventlist)

		#双方有可能打出了新的牌 对事件列表造成了改变 所以执行update
		self.update()
		#对双方正在时间轴上的法术进行时间操作
		self.player_a.usingcard.time -= 1
		self.player_b.usingcard.time -= 1
		#判断双方的法术发动时间是否达到
		if self.player_a.usingcard.time == 0:#玩家A的法术吟唱时间到 发动
			self.player_a.usingcard.caculate()
		if self.player_b.usingcard.time == 0:#玩家B的法术吟唱时间到 发动
			self.player_b.usingcard.caculate()
		#再次执行update函数
		self.update()
		#将结算消息发送给所有玩家
		self.sendtoAll(self.player_a.usingcard.describe())
		self.sendtoAll(self.player_b.usingcard.describe())
		self.sendtoAll(self.statereturn(self.player_a))
		self.sendtoAll(self.statereturn(self.player_b))
		self.player_a.usingcard.sendtoowner()
		self.player_b.usingcard.sendtoowner()
		self.sendtoa(self.player_a.info)
		self.sendtob(self.player_b.info)
		self.player_a.info = '没什么别的话要说了'
		self.player_b.info = '没什么别的话要说了'
		#双方的法术结算完毕 开始判断是否将usingcard参数归零
		# if self.player_a.usingcard.time == 0 and self.player_a.usingcard.name == '轮空':#玩家A的法术吟唱时间到 归零
		# 	self.player_a.cardbook.addcard(0, Lunkong())
		# 	self.player_a.cardbook.book[0].owner = self.player_a
		# 	self.player_a.usingcard = 0
		# if self.player_b.usingcard.time == 0 and self.player_b.usingcard.name == '轮空':#玩家B的法术吟唱时间到 归零
		# 	self.player_b.cardbook.addcard(0, Lunkong())
		# 	self.player_b.cardbook.book[0].owner = self.player_b
		# 	self.player_b.usingcard = 0
		if self.player_a.usingcard.time == 0:#玩家A的法术吟唱时间到 归零
			if self.player_a.usingcard.name == '轮空':
				self.player_a.cardbook.addcard(0, Lunkong())
				self.player_a.cardbook.book[0].owner = self.player_a
			self.player_a.usingcard = 0
		if self.player_b.usingcard.time == 0:#玩家B的法术吟唱时间到 归零
			if self.player_b.usingcard.name == '轮空':
				self.player_b.cardbook.addcard(0, Lunkong())
				self.player_b.cardbook.book[0].owner =self.player_b
			self.player_b.usingcard = 0
		
		self.sendtoAll('====================回合分割线====================')
		self.timewalk()
	#游戏开方法
	def gamestart(self):
		print '一局游戏开始了'
		self.startserver()
		print '游戏开始 端口号:' + str(self.port)
		time.sleep(3)
		self.chushihua()
		self.bindlists()
		c = 1
		while  True:
			
			self.oneround(c)
			c += 1
			if self.player_a.hp <= 0 and self.player_b.hp <= 0:
				self.sendtoAll('游戏结束 两位法师同归于尽')
				break
			if self.player_a.hp <= 0 and self.player_b.hp > 0:
				self.sendtoAll('游戏结束 ' + self.player_b.name + ' 赢得胜利！')
				break
			if self.player_b.hp <= 0 and self.player_a.hp >0:
				self.sendtoAll('游戏结束 ' + self.player_a.name + ' 赢得胜利！')
				break
			time.sleep(3)

		self.endserver()
		print '游戏结束'


if __name__ == '__main__':
	game = Game(1,2, 6000)
	game.gamestart()
	print 'done'
