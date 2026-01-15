import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

a = n // m
b = n % m

if b != 0 :
    print(a+1)
else :
    print(a)