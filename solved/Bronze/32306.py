import sys

x1, y1, z1 = map(int, sys.stdin.readline().rstrip().split())
x2, y2, z2 = map(int, sys.stdin.readline().rstrip().split())

t1score = 0
t2score = 0


t1score = (1*x1) + (2*y1) + (3*z1)
t2score = (1*x2) + (2*y2) + (3*z2)

if t1score == t2score :
    print("0")
elif t1score > t2score :
    print("1")
else :
    print("2")