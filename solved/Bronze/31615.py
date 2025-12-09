import sys

a = int(sys.stdin.readline().rstrip())
b = int(sys.stdin.readline().rstrip())

val = a + b

if (val < 10) :
    print(1)
elif(val >= 10 and val < 100) :
    print(2)
elif(val >= 100 and val < 1000) :
    print(3)