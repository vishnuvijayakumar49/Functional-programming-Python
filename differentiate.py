def differential(f):
	return lambda x:(f(x+0.001)-f(x))/0.001

def cube(x):
	return x*x*x

def sqr(x):
	return x*x

p=differential(cube)
p(3)
