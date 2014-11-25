import sys, gc, time
def make_cycle():
	l = {}
        for i in range(10):
		l[i]=1

def main():
	collected = gc.collect()
	#print "Collected %d objects" % (collected)
  	for i in range(10):
		make_cycle()
		collected = gc.collect()
 		print "collected %d objects" % (collected)
		time.sleep(1)
if __name__ == "__main__":
	ret = main()
	sys.exit(ret)

