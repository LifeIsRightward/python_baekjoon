import sys

tc = int(sys.stdin.readline().rstrip())

for _ in range(tc) :
    li = list(map(int, sys.stdin.readline().rstrip().split()))
    
    total = 0
    evenli = []

    for x in li :
        if x % 2 == 0 :
            evenli.append(x)
            total += x
        
    print(f"{total} {min(evenli)}")
