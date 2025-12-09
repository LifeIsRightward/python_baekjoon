import sys

s,a = map(int, sys.stdin.readline().rstrip().split())

s = s // 2
a = a // 2

print(min(s, a))
