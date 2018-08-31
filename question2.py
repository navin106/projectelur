import sys
'''
@author :navin106
finding the sum of the even numbers of fibbanoci starting from the 1
'''
def evenfib(n):
    a = 1
    b = 1
    k = []
    for i in range(n):
        c = a+b
        a = b
        b = c
        if c <= n:
            if c%2 == 0:
                k.append(c)
        else:
            break
    return sum(k)
        
def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(evenfib(n))
main()
