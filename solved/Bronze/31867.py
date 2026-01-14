import sys

n = int(sys.stdin.readline().rstrip())

li = sys.stdin.readline().rstrip()

odd = 0
even = 0

for x in li :
    if int(x) % 2 == 0 :
        even += 1
    else :
        odd += 1

if even == odd :
    print("-1")
elif even > odd :
    print("0")
else :
    print("1")