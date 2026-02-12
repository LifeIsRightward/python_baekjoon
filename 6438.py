import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n) :
    st = sys.stdin.readline().rstrip()
    print(st[::-1])
