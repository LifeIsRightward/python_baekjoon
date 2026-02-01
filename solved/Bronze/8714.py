import sys

n = int(sys.stdin.readline().rstrip())

li = list(map(int, sys.stdin.readline().rstrip().split()))

a = 0
b = 0

for x in li :
    if x == 1 :
        a +=1
    else :
        b += 1

if a > b :
    print(b)
else :
    print(a)