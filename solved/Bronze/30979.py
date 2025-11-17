import sys

time = int(sys.stdin.readline().rstrip())
candy = int(sys.stdin.readline().rstrip())

flavor = list(map(int, sys.stdin.readline().rstrip().split()))

total = 0

for i in range(candy) :
    total += flavor[i]

if total >= time :
    print("Padaeng_i Happy")
else :
    print("Padaeng_i Cry")