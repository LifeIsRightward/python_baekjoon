import sys

line = sys.stdin.readline().rstrip()

b = 0
c = 0

for x in line :
    if x == "B" :
        b += 1
    else:
        c += 1

print((b//2) + (c//2))
