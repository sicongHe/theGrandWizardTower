class jbjb(object):
	"""docstring for jbjb"""
	pass
class jb(object):
	"""docstring for jb"""
	pass
		
jbjb1 = jbjb()
jbjb2 = jbjb()
jb1 = jb()

jbjb1.a = jb1
jbjb2.b = jb1
jbjb1.a.q = 1
print jbjb2.b.q
print (jbjb1.a == jbjb2.b)