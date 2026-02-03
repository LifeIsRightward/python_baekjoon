import sys

li = list(map(int, sys.stdin.readline().rstrip().split()))

tmp = 0

for x in li :
    if x > 0 :
        tmp += 1

print(tmp)