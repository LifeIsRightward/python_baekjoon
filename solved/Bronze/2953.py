import sys

li = []

for i in range(1,6,1) :
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))

    total = 0
    for x in tmp :
        total += x
    
    li.append((i,total))

li.sort(key=lambda x: x[1], reverse=True)

print(f"{li[0][0]} {li[0][1]}")



