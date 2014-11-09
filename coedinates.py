class cordinate:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __repr__(self):
		return "cordnt :"+str(self.__dict__)

def add(a1,a2,b1,b2):
	a=cordinate(a1,a2)
	b=cordinate(b1,b2)
	return cordinate(a.x+b.x,a.y+b.y)

def sub(a1,a2,b1,b2):
	a=cordinate(a1,a2)
	b=cordinate(b1,b2)
	return cordinate(a.x-b.x,a.y-b.y)



print add(1,2,3,4)
print sub(1,2,3,4)
