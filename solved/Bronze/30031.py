import sys

n = int(sys.stdin.readline().rstrip())

total = 0

for i in range(n) :
    x, y = list(map(int, sys.stdin.readline().rstrip().split()))

    if x == 136 :
        total += 1000
    elif x == 142 :
        total += 5000
    elif x == 148 :
        total += 10000
    else :
        total += 50000

print(total)