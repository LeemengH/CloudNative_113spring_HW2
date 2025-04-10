import sys

if __name__ == '__main__':
	if sys.argv[1] == "case1":
		print("hw1-p case1 execute correctly!")
	elif sys.argv[1] == "case2":
		print("hw1-p case2 execute correctly!")
	else:
		raise Exception("Unknown case....")
