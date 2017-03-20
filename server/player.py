#!/usr/bin/env python
# -*- coding:utf-8 -*-
from race import *
from cardbook import *
from card import *
import copy
class Player(object):
	def __init__(self):
		self.hp = 40
		self.defence = 1
		self.cardbook = 0
		self.usingcard = 0
		self.yc = 0
		self.info = '没什么别的话要说了'
	def setname(self,name):
		self.name = name
	def usecard(self, card):
		self.usingcard = card
	def setcardbook(self,cardbook):
		self.cardbook = cardbook
		self.cardbook.owner = self
		self.bookback = copy.deepcopy(self.cardbook)



if __name__ == '__main__':
	print 'Player.py test'
	a = Player()