import sys

x, y = map(int, sys.stdin.readline().rstrip().split())
a = []
b = []

for i in range(x) :
    a.append(1)

for j in range(y) :
    b.append(1)

aresult = int("".join(map(str, a)))
bresult = int("".join(map(str, b)))

print(aresult+bresult)