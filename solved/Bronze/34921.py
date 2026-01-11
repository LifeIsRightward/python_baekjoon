import sys

a, t = map(int, sys.stdin.readline().rstrip().split())

p = 10 + 2 * (25-a+t)

if p > 0 :
    print(p)
else :
    print("0")