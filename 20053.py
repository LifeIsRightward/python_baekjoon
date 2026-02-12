import sys

tc = int(sys.stdin.readline().rstrip())

for i in range(tc):
    n = int(sys.stdin.readline().rstrip())
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    print(f"{min(li)} {max(li)}")