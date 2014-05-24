"""shared dict"""

import threading

def webworker(a):
	return lambda f : f

@webworker( 'xxx.js' )
def mythread(a,b, lowlevel):
	## checks a and b, if they are Array, then wrap them.
	print(a)
	print(b)
	if lowlevel:  ## workaround for javascript mode
		a.__setitem__('x', 'hello')
		b.__setitem__('y', 'world')
	else:
		a[ 'x' ] = 'hello'
		b[ 'y' ] = 'world'

def main():
	if PYTHON != "PYTHONJS":
		threading.start_new_thread = threading._start_new_thread

	shared1 = {}
	shared2 = {'z':100}

	t = threading.start_new_thread( mythread, (shared1, shared2, BACKEND=='JAVASCRIPT') )

	ticks = 0
	while len(shared1) + len(shared2) < 2:
		ticks += 1
		if ticks > 1000:  ## do not hangup if there is a bug in the webworker
			break

	TestError( shared1['x'] == 'hello' )
	TestError( shared2['y'] == 'world' )
	TestError( shared2['z'] == 100 )

