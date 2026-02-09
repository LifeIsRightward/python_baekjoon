import sys

n = input()
li = list(map(int, sys.stdin.readline().rstrip().split()))

li.sort()
print(li[len(li)-1])