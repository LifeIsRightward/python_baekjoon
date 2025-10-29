import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

if a >= b :
    print(a-b-1)
    
    for i in range(b+1, a) :
        print(i, end=" ")
elif a < b :
    print(b-a-1)

    for j in range(a+1, b) :
        print(j, end=" ")




