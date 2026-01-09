import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))

# d는 공차
d = li[1] - li[0]

print(li[len(li)-1] + d)