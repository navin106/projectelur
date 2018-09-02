"""
@author: navin106
date: 01:sep:2018 12:27 AM
"""
import math
def lrgprime(inp_no):
	# print(inp_no)
	large = 0
	for i in range(1,inp_no+1):
		# print(i)
		cnt = 0
		# print(inp_no%i)
		if inp_no%i == 0:
			# print(int(round(math.sqrt(i), 0)))
			for j in range(1,(i//2)+1):
				if i%j == 0:
					cnt += 1
			# print(cnt)
			if cnt == 1:
				large = i
	return large
def main():
	k = int(input())
	res  = [int(input()) for i in range(k)]
	for inp_no in res:
		print(lrgprime(inp_no))
main()
