a_string="this is not a global variable"
def foo():
	a_string="new string"

	print a_string
	print locals()

foo()
print a_string
