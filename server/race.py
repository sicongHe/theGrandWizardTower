#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
class Race(object):
	pass

class Human(Race):
	def __init__(self):
		self.race = '人类'
		self.intelligence = 0
		self.constitution = 0
		self.charisma = 0
		self.dexterity = 0
		self.willpower = 0
		self.size = 0
	def setsize(self,size):
		self.size = size
	def getintelligence(self):
		return self.intelligence
	def getconstitution(self):
		return self.constitution
	def getcharisma(self):
		return self.charisma
	def getdexterity(self):
		return self.dexterity
	def getwillpower(self):
		return self.willpower
	def  getsize(self):
		return self.size
	def getall(self):
		return '智力:' + str(self.getintelligence()) + '\n' + '体质:' + str(self.getconstitution()) + '\n' + '魅力:' + str(self.getcharisma()) + '\n' + '专注:' + str(self.getwillpower()) + '\n' + '敏捷:' + str(self.getdexterity()) + '\n' + '体型:' + self.getsize()
	
	def roll(self):
		self.intelligence = random.randrange(7,11,1)
		self.constitution = random.randrange(7,11,1)
		self.charisma = random.randrange(7,11,1)
		self.dexterity = random.randrange(7,11,1)
		self.willpower = random.randrange(7,11,1)

class Elf(Race):
	def __init__(self):
		self.race = '精灵'
		self.intelligence = 0
		self.constitution = 0
		self.charisma = 0
		self.dexterity = 0
		self.willpower = 0
		self.size = 0
	def setsize(self,size):
		self.size = size
	def getintelligence(self):
		return self.intelligence
	def getconstitution(self):
		return self.constitution
	def getcharisma(self):
		return self.charisma
	def getdexterity(self):
		return self.dexterity
	def getwillpower(self):
		return self.willpower
	def  getsize(self):
		return self.size
	def getall(self):
		return '智力:' + str(self.getintelligence()) + '\n' + '体质:' + str(self.getconstitution()) + '\n' + '魅力:' + str(self.getcharisma()) + '\n' + '专注:' + str(self.getwillpower()) + '\n' + '敏捷:' + str(self.getdexterity()) + '\n' + '体型:' + self.getsize()
	
	def roll(self):
		self.intelligence = random.randrange(7,12,1)
		self.constitution = random.randrange(5,8,1)
		self.charisma = random.randrange(9,15,1)
		self.dexterity = random.randrange(8,12,1)
		self.willpower = random.randrange(7,10,1)

class Cave(Race):
	def __init__(self):
		self.race = '穴居人'
		self.intelligence = 0
		self.constitution = 0
		self.charisma = 0
		self.dexterity = 0
		self.willpower = 0
		self.size = 0
	def setsize(self,size):
		self.size = size
	def getintelligence(self):
		return self.intelligence
	def getconstitution(self):
		return self.constitution
	def getcharisma(self):
		return self.charisma
	def getdexterity(self):
		return self.dexterity
	def getwillpower(self):
		return self.willpower
	def  getsize(self):
		return self.size
	def getall(self):
		return '智力:' + str(self.getintelligence()) + '\n' + '体质:' + str(self.getconstitution()) + '\n' + '魅力:' + str(self.getcharisma()) + '\n' + '专注:' + str(self.getwillpower()) + '\n' + '敏捷:' + str(self.getdexterity()) + '\n' + '体型:' + self.getsize()
	
	def roll(self):
		self.intelligence = random.randrange(7,11,1)
		self.constitution = random.randrange(4,6,1)
		self.charisma = random.randrange(3,5,1)
		self.dexterity = random.randrange(10,13,1)
		self.willpower = random.randrange(10,13,1)
class Robot(Race):
	def __init__(self):
		self.race = '构装生物'
		self.intelligence = 0
		self.constitution = 0
		self.charisma = 0
		self.dexterity = 0
		self.willpower = 0
		self.size = 0
	def setsize(self,size):
		self.size = size
	def getintelligence(self):
		return self.intelligence
	def getconstitution(self):
		return self.constitution
	def getcharisma(self):
		return self.charisma
	def getdexterity(self):
		return self.dexterity
	def getwillpower(self):
		return self.willpower
	def  getsize(self):
		return self.size
	def getall(self):
		return '智力:' + str(self.getintelligence()) + '\n' + '体质:' + str(self.getconstitution()) + '\n' + '魅力:' + str(self.getcharisma()) + '\n' + '专注:' + str(self.getwillpower()) + '\n' + '敏捷:' + str(self.getdexterity()) + '\n' + '体型:' + self.getsize()
	
	def roll(self):
		self.intelligence = random.randrange(5,8,1)
		self.constitution = random.randrange(12,16,1)
		self.charisma = random.randrange(1,11,1)
		self.dexterity = random.randrange(1,3,1)
		self.willpower = random.randrange(5,8,1)


if __name__ == '__main__':
	print 'test'
	human = Elf()
	size = raw_input('size:')
	human.setsize(size)
	j = raw_input('roll?')
	while j == 'roll':
		human.roll()
		print human.getall()
		j = raw_input('roll?')




