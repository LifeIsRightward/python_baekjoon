import sys

n = int(sys.stdin.readline())

li = []

for i in range(n) :
    li.append(int(sys.stdin.readline()))

cute = 0
nocute = 0
for x in li :
    if x == 0 :
        nocute += 1
    else :
        cute += 1

if nocute > cute :
    print("Junhee is not cute!")
else :
    print("Junhee is cute!")