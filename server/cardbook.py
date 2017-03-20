#!/usr/bin/env python
# -*- coding:utf-8 -*-
from card import *
from player import *
import copy
class Cardbook(object):
	"""docstring for Cardbook"""
	def __init__(self):
		self.book = {}
		self.owner = 0
		pass
	def setowner(self, owner):
		self.owner = owner
		for k in self.book:
			self.book[k].owner = self.owner
			print self.owner.name + self.book[k].name
	def addcard(self,num,card):
		self.book[num] = card
	def usecard(self,num):
		self.tmpcard = self.book[num]
		self.pop = num
		self.tmpcard.use()
		return self.tmpcard
	def update(self):
		self.book.pop(self.pop)
		
		