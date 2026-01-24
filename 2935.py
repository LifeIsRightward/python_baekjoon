import sys

a = int(sys.stdin.readline().rstrip())
b = sys.stdin.readline().rstrip()
c = int(sys.stdin.readline().rstrip())

if b == '*' :
    print(a * c)
else :
    print(a + c)