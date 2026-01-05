import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))


minn = li[0]

for x in li :
    if minn > x :
        minn = x

print(li.index(minn))