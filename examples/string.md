String
------
the c++ backend translates strings into `std::string`.

```rusthon

myglobal = 'hi'
def main():
	u = 'X'
	print len(u)

	a = 'XYZ'
	print( a[0] == 'X' )
	print( a[-1] == 'Z' )
	print myglobal[-1]

	#print( a[0:2] == 'XY' )


	print 'ok'

```