import sys

n = int(sys.stdin.readline().rstrip())

li = []
for i in range(n) :
    li.append(int(sys.stdin.readline().rstrip()))


minv = min(li)
maxv = max(li)

if li[0] == minv :
    print("ez")
elif li[0] == maxv :
    print("hard")
else :
    print("?")

