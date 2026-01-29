import sys

def T(n) :
    tmp = 0
    for i in range(1, n+1) :
        tmp += i
    return tmp

tc = int(sys.stdin.readline().rstrip())

for i in range(tc) :
    n = int(sys.stdin.readline().rstrip())

    wn = 0
    for i in range(1, n+1) :
        wn += (i*T(i+1))
    print(wn)

