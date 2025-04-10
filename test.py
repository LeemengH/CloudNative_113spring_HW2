import sys

if __name__ == '__main__':
	if sys.argv[1] == "case1":
		print("case1 execute correctly!")
	elif sys.argv[1] == "case2":
		raise Exception("Wrong execution....")
	else:
		raise Exception("Unknown case....")
