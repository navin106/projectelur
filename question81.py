
def shortpath(k):
	sum = 0
	j = 0
	for i in range(len(k)-2):
		if i%2 == 0:
			print(j)
			print(int(k[j][j]), int(k[j+1][j]), int(k[j+1][j+1]))
			sum += int(k[j][j]) +int(k[j+1][j]) +int(k[j+1][j+1])
			j+=1
		else:
			print(j)
			print(int(k[j][j+1]), int(k[j+1][j+1]), int(k[j+1][j+2]))
			sum += int(k[j][j+1]) +int(k[j+1][j+1]) +int(k[j+1][j+2])
			j+=2
	# print(int(k[j][j]), int(k[j+1][j]), int(k[j+1][j+1]))
	return sum
def cremat(n):
	k = []
	for _ in range(n):
		k.append((input()).split())
	return shortpath(k)

def main():
	rowcol = int(input())
	print(cremat(rowcol))
main()