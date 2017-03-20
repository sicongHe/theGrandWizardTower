#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tools import *
import copy
class Card(object):
	"""docstring for Card"""
	def sendtoowner(self):
		pass

#魔法飞弹类
class Mofafeidan(Card):
	def __init__(self):
		print '魔法飞弹正在初始化'
		self.name = '魔法飞弹'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 2
		self.timeout = 0
		self.counterspell = False
		self.useful = True
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		for i in self.lists:
			if i.name == 'Counterspell':
				i.addlistener(self)
				self.listenlist = i
	def registereventlist(self):
		pass

	def use(self):#打出该张卡牌的函数
		print self.owner.name + '打出了' + self.name
		self.registerlistenlist()
		pass

	def update(self):#update中的操作有两种 检测表中的事件来判断自己应该做什么 或者来判断自己还是否应该呆在表中
		print self.name + '接到通知'
		self.counterspell = False
		for i in self.listenlist.events:
			print i.name
			if i.name == '反制' and i.owner != self.owner and i.useful == True:
				print self.name + ' 遭到反制'
				self.counterspell = True
				break
		if self.timeout == -1:
			print self.name + '被从列表中抛出'
			self.useful = False

	def caculate(self):#发动该张卡牌的函数
		if self.counterspell == False:
			self.hurt = (3 - self.enemey.defence)
		else:
			print self.owner.name + ' 遭到反制'
			self.owner.hp -= 1
			self.hurt = 0

		self.enemey.hp = self.enemey.hp - self.hurt
		self.timeout -= 1



	def describe(self):
		if self.time != 0:
			self.owner.yc += 1
			return self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
		else:
			self.owner.yc = 0
			if self.counterspell == True:
				return self.owner.name + ' 试图释放' + self.name + ' 被' + self.enemey.name + ' 成功反制！' + self.owner.name + ' 惊慌失措！'
			else:
				return self.owner.name + ' 发动了' + self.name + ' 对 ' + self.enemey.name + ' 造成了 ' + str(self.hurt) + ' 点伤害 要小心了！'


#马友夫微流星类
class Mayoufuweiliuxing(Card):
	def __init__(self):
		self.name = '马友夫微流星'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 3
		self.timeout = 0
		self.counterspell = False
		self.useful = True
		print self.name + '正在初始化'
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		for i in self.lists:
			if i.name == 'Counterspell':
				i.addlistener(self)
				self.listenlist = i
	def registereventlist(self):
		pass

	def use(self):#打出该张卡牌的函数
		print self.owner.name + '打出了' + self.name
		self.registerlistenlist()
		pass

	def update(self):#update中的操作有两种 检测表中的事件来判断自己应该做什么 或者来判断自己还是否应该呆在表中
		print self.name + '接到通知'
		self.counterspell = False
		for i in self.listenlist.events:
			print i.name
			if i.name == '反制' and i.owner != self.owner and i.useful == True:
				print self.name + ' 遭到反制'
				self.counterspell = True
				break
		if self.timeout == -1:
			print self.name + '被从列表中抛出'
			self.useful = False

	def caculate(self):#发动该张卡牌的函数
		if self.counterspell == False:
			self.hurt = (4 - self.enemey.defence)
		else:
			print self.owner.name + ' 遭到反制'
			self.owner.hp -= 2
			self.hurt = 0

		self.enemey.hp = self.enemey.hp - self.hurt
		self.timeout -= 1


	def describe(self):
		if self.time != 0:
			self.owner.yc += 1
			return self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
		else:
			self.owner.yc = 0
			if self.counterspell == True:
				return self.owner.name + ' 试图释放' + self.name + ' 被' + self.enemey.name + ' 成功反制！' + self.owner.name + ' 惊慌失措！'
			else:
				return self.owner.name + ' 发动了' + self.name + ' 对 ' + self.enemey.name + ' 造成了 ' + str(self.hurt) + ' 点伤害 要小心了！'

#摩丘利亚之光类
class Moqiuliyazhiguang(Card):
	def __init__(self):
		self.name = '摩丘利亚之光'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 4
		self.timeout = 0
		self.counterspell = False
		self.useful = True
		print self.name + '正在初始化'
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		for i in self.lists:
			if i.name == 'Counterspell':
				i.addlistener(self)
				self.listenlist = i
	def registereventlist(self):
		pass

	def use(self):#打出该张卡牌的函数
		print self.owner.name + '打出了' + self.name
		self.registerlistenlist()
		pass

	def update(self):#update中的操作有两种 检测表中的事件来判断自己应该做什么 或者来判断自己还是否应该呆在表中
		print self.name + '接到通知'
		self.counterspell = False
		for i in self.listenlist.events:
			print i.name
			if i.name == '反制' and i.owner != self.owner and i.useful == True:
				print self.name + ' 遭到反制'
				self.counterspell = True
				break
		if self.timeout == -1:
			print self.name + '被从列表中抛出'
			self.useful = False

	def caculate(self):#发动该张卡牌的函数
		if self.counterspell == False:
			self.hurt = (6 - self.enemey.defence)
		else:
			print self.owner.name + ' 遭到反制'
			self.owner.hp -= 3
			self.hurt = 0

		self.enemey.hp = self.enemey.hp - self.hurt
		self.timeout -= 1


	def describe(self):
		if self.time != 0:
			self.owner.yc += 1
			return self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
		else:
			self.owner.yc = 0
			if self.counterspell == True:
				return self.owner.name + ' 试图释放' + self.name + ' 被' + self.enemey.name + ' 成功反制！' + self.owner.name + ' 惊慌失措！'
			else:
				return self.owner.name + ' 发动了' + self.name + ' 对 ' + self.enemey.name + ' 造成了 ' + str(self.hurt) + ' 点伤害 要小心了！'


#大崩灭术类
class Dabengmieshu(Card):
	def __init__(self):
		
		self.name = '大崩灭术'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 5
		self.timeout = 0
		self.counterspell = False
		self.useful = True
		print self.name + '正在初始化'
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		for i in self.lists:
			if i.name == 'Counterspell':
				i.addlistener(self)
				self.listenlist = i
	def registereventlist(self):
		pass

	def use(self):#打出该张卡牌的函数
		print self.owner.name + '打出了' + self.name
		self.registerlistenlist()
		pass

	def update(self):#update中的操作有两种 检测表中的事件来判断自己应该做什么 或者来判断自己还是否应该呆在表中
		print self.name + '接到通知'
		self.counterspell = False
		for i in self.listenlist.events:
			print i.name
			if i.name == '反制' and i.owner != self.owner and i.useful == True:
				print self.name + ' 遭到反制'
				self.counterspell = True
				break
		if self.timeout == -1:
			print self.name + '被从列表中抛出'
			self.useful = False

	def caculate(self):#发动该张卡牌的函数
		if self.counterspell == False:
			self.hurt = (9 - self.enemey.defence)
		else:
			print self.owner.name + ' 遭到反制'
			self.hurt = 0
			self.owner.hp -= 4

		self.enemey.hp = self.enemey.hp - self.hurt
		self.timeout -= 1


	def describe(self):
		if self.time != 0:
			self.owner.yc += 1
			return self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
		else:
			self.owner.yc = 0
			if self.counterspell == True:
				return self.owner.name + ' 试图释放' + self.name + ' 被' + self.enemey.name + ' 成功反制！' + self.owner.name + ' 惊慌失措！'
			else:
				return self.owner.name + ' 发动了' + self.name + ' 对 ' + self.enemey.name + ' 造成了 ' + str(self.hurt) + ' 点伤害 要小心了！'

#马友夫强酸箭类
class Mayoufuqiangsuanjian(Card):
	def __init__(self):
		
		self.name = '马友夫强酸箭'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 4
		self.timeout = 0
		self.counterspell = False
		self.useful = True
		print self.name + '正在初始化'
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		for i in self.lists:
			if i.name == 'Counterspell':
				i.addlistener(self)
				self.listenlist = i
	def registereventlist(self):
		pass

	def use(self):#打出该张卡牌的函数
		print self.owner.name + '打出了' + self.name
		self.registerlistenlist()
		pass

	def update(self):#update中的操作有两种 检测表中的事件来判断自己应该做什么 或者来判断自己还是否应该呆在表中
		print self.name + '接到通知'
		self.counterspell = False
		for i in self.listenlist.events:
			print i.name
			if i.name == '反制' and i.owner != self.owner and i.useful == True:
				print self.name + ' 遭到反制'
				self.counterspell = True
				break
		if self.timeout == -1:
			print self.name + '被从列表中抛出'
			self.useful = False

	def caculate(self):#发动该张卡牌的函数
		if self.counterspell == False:
			self.hurt = (3 - self.enemey.defence)
			self.enemey.defence = 0
		else:
			print self.owner.name + ' 遭到反制'
			self.owner.hp -= 3
			self.hurt = 0

		self.enemey.hp = self.enemey.hp - self.hurt
		
		self.timeout -= 1


	def describe(self):
		if self.time != 0:
			self.owner.yc += 1
			return self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
		else:
			self.owner.yc = 0
			if self.counterspell == True:
				return self.owner.name + ' 试图释放' + self.name + ' 被' + self.enemey.name + ' 成功反制！' + self.owner.name + ' 惊慌失措！'
			else:
				return self.owner.name + ' 发动了' + self.name + ' 对 ' + self.enemey.name + ' 造成了 ' + str(self.hurt) + ' 点伤害 要小心了！' + '同时腐蚀了一点防御力！'


#反制类
class Fanzhi(Card):
	"""docstring for Card"""
	def __init__(self):
		print '反制正在初始化'
		self.name = '反制'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 1
		self.timeout = 0
		self.useful = True
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		"""在这里加入该法术需要监听的列表"""
		pass

	def registereventlist(self):
		for i in self.lists:
			if i.name == 'Counterspell':
				i.addevent(self)
				self.eventlist = i

	def update(self):
		print self.owner.name + '反制接到通知'
		if self.timeout == -1:
			self.useful = False
			print self.owner.name + ' 反制已经抛出'
	def use(self):#打出该张卡的函数
		print self.owner.name + '打出了' + self.name
		self.registereventlist()

	def caculate(self):
		self.timeout -= 1
		pass


	def describe(self):
		return self.owner.name + ' 发动了法术反制！'


#冥想类
class Mingxiang(Card):
	"""docstring for Mingxiang"""
	def __init__(self):
		print '冥想正在初始化'
		self.name = '冥想'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 5
		self.timeout = 0
		self.counterspell = False
		self.useful = True
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		pass
	def registereventlist(self):
		pass
	def use(self):#打出该张卡牌的函数
		print self.owner.name + '打出了' + self.name
		self.registerlistenlist()
		pass
	def update(self):
		print '冥想接到通知'
		pass
	def caculate(self):
		self.owner.cardbook = copy.deepcopy(self.owner.bookback)
		for i in self.owner.cardbook.book:
			self.owner.cardbook.book[i].owner = self.owner
			self.owner.cardbook.book[i].enemey = self.enemey
			self.owner.cardbook.book[i].lists = self.lists
		print self.owner.name + ' 恢复了所有法术！'
	def describe(self):
		if self.time != 0:
			self.owner.yc += 1
			return self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
		else:
			self.owner.yc += 1
			tmp = self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
			return tmp

#轮空类
class Lunkong(Card):
	"""docstring for Mingxiang"""
	def __init__(self):
		print '轮空正在初始化'
		self.name = '轮空'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 1
		self.timeout = 0
		self.counterspell = False
		self.useful = True
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		pass
	def registereventlist(self):
		pass
	def use(self):#打出该张卡牌的函数
		print self.owner.name + '打出了' + self.name
		self.registerlistenlist()
		pass
	def update(self):
		print '轮空接到通知'
		pass
	def caculate(self):
		pass
	def describe(self):
		# self.owner.cardbook.book[0] = self
		# self.owner.cardbook.book[0].time = 1
		if self.time != 0:
			self.owner.yc += 1
			return self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
		else:
			self.owner.yc += 1
			tmp = self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
			return tmp

#能量塑造类
class Nengliangsuzao(Card):
	def __init__(self):
		print '能量塑造正在初始化'
		self.name = '能量塑造'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 3
		self.timeout = 10000
		self.counterspell = False
		self.useful = True
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		for i in self.lists:
			if i.name == 'Counterspell':
				i.addlistener(self)
				self.listenlist = i
	def registereventlist(self):
		for i in self.lists:
			if i.name == 'Counterspell':
				i.addevent(self)
				self.eventlist = i

	def use(self):#打出该张卡牌的函数
		print self.owner.name + '打出了' + self.name
		self.registerlistenlist()
		pass

	def update(self):#update中的操作有两种 检测表中的事件来判断自己应该做什么 或者来判断自己还是否应该呆在表中
		print self.name + '接到通知'
		self.counterspell = False
		for i in self.listenlist.events:
			print i.name
			if i.name == '反制' and i.owner != self.owner and i.useful == True:
				print self.name + ' 遭到反制'
				self.counterspell = True
				break
		if self.timeout == -1:
			print self.name + '被从列表中抛出'
			self.useful = False

	def caculate(self):#发动该张卡牌的函数
		if self.counterspell == False:
			print self.owner.name + '获得了一个能量块'
			self.registereventlist()
		else:
			print self.owner.name + ' 遭到反制'
			self.owner.hp -= 2

	def sendtoowner(self):
		if self.time == 0 and self.counterspell == False:
			total = 0
			for i in self.eventlist.events:
				if i.name == '能量塑造' and i.owner == self.owner:
					total += 1
			total = str(total)
			self.owner.info = '你拥有能量块总数为 ' + total + ' 让敌人在元素的力量面前颤抖吧！'
			print self.owner.name + self.owner.info

	def describe(self):
		if self.time != 0:
			self.owner.yc += 1
			return self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
		else:
			self.owner.yc = 0
			if self.counterspell == True:
				return self.owner.name + ' 试图进行一个魔法仪式' + ' 被' + self.enemey.name + ' 成功反制！' + self.owner.name + ' 惊慌失措！'
			else:
				return self.owner.name + ' 完成了一个神秘的仪式 要小心了'

#火龙卷类
class Huolongjuan(Card):
	def __init__(self):
		print '火龙卷正在初始化'
		self.name = '火龙卷'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 4
		self.timeout = 0
		self.counterspell = False
		self.useful = True
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		for i in self.lists:
			if i.name == 'Counterspell':
				i.addlistener(self)
				self.listenlist = i
	def registereventlist(self):
		pass

	def use(self):#打出该张卡牌的函数
		print self.owner.name + '打出了' + self.name
		self.registerlistenlist()
		pass

	def update(self):#update中的操作有两种 检测表中的事件来判断自己应该做什么 或者来判断自己还是否应该呆在表中
		print self.name + '接到通知'
		self.counterspell = False
		for i in self.listenlist.events:
			print i.name
			if i.name == '反制' and i.owner != self.owner and i.useful == True:
				print self.name + ' 遭到反制'
				self.counterspell = True
				break
		if self.timeout == -1:
			print self.name + '被从列表中抛出'
			self.useful = False

	def caculate(self):#发动该张卡牌的函数
		self.hurt = 0
		if self.counterspell == False:
			for i in self.listenlist.events:
				if i.name == '能量塑造' and i.useful == True and i.owner == self.owner:
					print '搜索到一个能量块'
					self.hurt = (14 - self.enemey.defence)
					i.useful = False
					print '将能量块用掉'
		else:
			for i in self.listenlist.events:
				if i.name == '能量塑造' and i.useful == True and i.owner == self.owner:
					print '搜索到一个能量块'
					self.hurt = (14 - self.enemey.defence)
					i.useful = False
					print '虽然被反制了 但依然将能量块用掉'
			self.owner.hp -= 3
			self.hurt = 0

		self.enemey.hp = self.enemey.hp - self.hurt
		self.timeout -= 1



	def describe(self):
		if self.time != 0:
			self.owner.yc += 1
			return self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
		else:
			self.owner.yc = 0
			if self.counterspell == True:
				return self.owner.name + ' 试图释放' + self.name + ' 被' + self.enemey.name + ' 成功反制！' + self.owner.name + ' 惊慌失措！'
			else:
				return self.owner.name + ' 发动了' + self.name + ' 对 ' + self.enemey.name + ' 造成了 ' + str(self.hurt) + ' 点伤害 要小心了！'

#雷霆地狱类
class Leitingdiyu(Card):
	def __init__(self):
		print '雷霆地狱正在初始化'
		self.name = '雷霆地狱'
		self.owner = 0
		self.enemey = 0
		self.listenlist = 0
		self.eventlist = 0
		self.time = 5
		self.timeout = 0
		self.counterspell = False
		self.useful = True
	def bindlists(self, lists):
		self.lists = lists
	def registerlistenlist(self):
		for i in self.lists:
			if i.name == 'Counterspell':
				i.addlistener(self)
				self.listenlist = i
	def registereventlist(self):
		pass

	def use(self):#打出该张卡牌的函数
		print self.owner.name + '打出了' + self.name
		self.registerlistenlist()
		pass

	def update(self):#update中的操作有两种 检测表中的事件来判断自己应该做什么 或者来判断自己还是否应该呆在表中
		print self.name + '接到通知'
		self.counterspell = False
		for i in self.listenlist.events:
			print i.name
			if i.name == '反制' and i.owner != self.owner and i.useful == True:
				print self.name + ' 遭到反制'
				self.counterspell = True
				break
		if self.timeout == -1:
			print self.name + '被从列表中抛出'
			self.useful = False

	def caculate(self):#发动该张卡牌的函数
		self.hurt = 0
		if self.counterspell == False:
			for i in self.listenlist.events:
				if i.name == '能量塑造' and i.useful == True and i.owner == self.owner:
					print '搜索到一个能量块'
					self.hurt = (16 - self.enemey.defence)
					i.useful = False
					print '将能量块用掉'
		else:
			for i in self.listenlist.events:
				if i.name == '能量塑造' and i.useful == True and i.owner == self.owner:
					print '搜索到一个能量块'
					self.hurt = (14 - self.enemey.defence)
					i.useful = False
					print '虽然被反制了 但依然将能量块用掉'
			self.owner.hp -= 4
			self.hurt = 0

		self.enemey.hp = self.enemey.hp - self.hurt
		self.timeout -= 1



	def describe(self):
		if self.time != 0:
			self.owner.yc += 1
			return self.owner.name + ' 正在吟唱！ ' + self.owner.name + ' 已经吟唱了 ' + str(self.owner.yc) + ' 回合 要小心了！'
		else:
			self.owner.yc = 0
			if self.counterspell == True:
				return self.owner.name + ' 试图释放' + self.name + ' 被' + self.enemey.name + ' 成功反制！' + self.owner.name + ' 惊慌失措！'
			else:
				return self.owner.name + ' 发动了' + self.name + ' 对 ' + self.enemey.name + ' 造成了 ' + str(self.hurt) + ' 点伤害 要小心了！'



if __name__ == '__main__':
	a = Card()
	b = Card()
	print a==a