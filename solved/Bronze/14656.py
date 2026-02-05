import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))

i = 1
tmp = 0

for x in li :
    if i != x :
        tmp += 1
    i +=1

print(tmp)
