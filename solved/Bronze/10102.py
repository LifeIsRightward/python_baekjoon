import sys

n = int(sys.stdin.readline().rstrip())

li = sys.stdin.readline().rstrip()

a = 0
b = 0

for x in li :
    if x == 'A' :
        a += 1
    else :
        b +=1

if a == b :
    print("Tie")
elif a > b :
    print("A")
else :
    print("B")