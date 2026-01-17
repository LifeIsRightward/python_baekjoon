import sys

n = int(sys.stdin.readline().rstrip())
work = int(sys.stdin.readline().rstrip())

total = 0

total += n * 10

if n >= 3 :
    total += 20
    if n == 5 :
        total += 50


if work > 1000 :
    total -= 15

if total > 0 :
    print(total)
else :
    print("0")