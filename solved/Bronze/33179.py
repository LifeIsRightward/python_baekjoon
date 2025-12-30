import sys

def cut(val) :
    if val % 2 != 0 :
        return (val // 2) + 1
    else :
        return val // 2
    
total = 0

n = int(sys.stdin.readline().rstrip())
raw = map(cut, map(int, sys.stdin.readline().rstrip().split()))

for x in raw :
    total += x

print(total)