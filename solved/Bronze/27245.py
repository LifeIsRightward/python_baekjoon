import sys

w = int(sys.stdin.readline().rstrip())
l = int(sys.stdin.readline().rstrip())
h = int(sys.stdin.readline().rstrip())


if min(w, l) >= h * 2 :
    condition1 = True
else :
    condition1 = False

if max(w, l) * 2  >= min(w, l) :
    condition2 = True
else :
    condition2 = False

if condition2 and condition1 :
    print("good")
else :
    print("bad")