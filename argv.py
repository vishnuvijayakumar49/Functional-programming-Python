def fun(*args):
	print args

def double(*args):
	print [int(arg)*2 for arg in args]



double(1,2,3)
double(2,3,4,5,7)
fun(1,2,3)
