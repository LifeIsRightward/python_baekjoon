import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n) :
    m = int(sys.stdin.readline().rstrip())
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    
    tmp = 0
    
    for x in li :
        tmp += x
    
    print(tmp)
