import sys
#!/bin/python3
'''
@author :navin106
'''
t = int(input().strip())
for a0 in range(t):
    s = 0
    n = int(input().strip())-1
    a = [i for i in range(n, n-20, -1) if i%3 == 0 ] #last numbers in the list of multiples of 3
    b = [i for i in range(n, n-20, -1) if i%5 == 0 ] #last numbers in the list of multiples of 5
    c = [i for i in range(n, n-20, -1) if i%15 == 0] #last numbers in the list of multiples of 15
    lena = 1+ ((a[0]-3)//3) #finding the length of the list of list multiples of 3
    lenb = 1+ ((b[0]-5)//5) #finding the length of the list of list multiples of 5
    lenc = 1+ ((c[0]-15)//15) #finding the length of the list of list multiples of 15
    sa = (lena*(3+a[0]))//2 #finding the sum of the list of 3 multiples
    sb = (lenb*(5+b[0]))//2 #finding the sum of the list of 5 multiples
    sc = (lenc*(15+c[0]))//2 #finding the sum of the list of 15 multiples
    s = sa+sb-sc #finding the final result of the sum of 3 and 5 multiples and \
                  #subtracting the multiples of 15 because it is repeated again
    print(s)