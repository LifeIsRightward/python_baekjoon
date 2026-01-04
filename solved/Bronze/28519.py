import sys

x, y = map(int, sys.stdin.readline().rstrip().split())
small = min(x, y)
big = max(x, y)

print(min(x+y, small*2 + 1))
