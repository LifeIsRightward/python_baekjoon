import sys
import math

x, y = map(int, sys.stdin.readline().rstrip().split())

total = math.ceil(((x * y) / 4840) / 5)

print(total)