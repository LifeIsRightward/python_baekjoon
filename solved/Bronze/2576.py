import sys

li = []

for _ in range(7) :
    tmp = int(sys.stdin.readline().rstrip())
    
    if tmp % 2 != 0 :
        li.append(tmp)

if len(li) == 0 :
    print("-1")
else :
    total = 0
    for x in li :
        total += x
    print(total)
    li.sort()
    print(li[0])

