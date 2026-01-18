import sys

y, c, p = map(int, sys.stdin.readline().rstrip().split())

c = c//2

print(min(y, c, p))