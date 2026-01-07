import sys

def grade(x) :
    grd = (x * 100) // n
    rgrd = 0

    if grd >= 0 and grd <= 4 :
        rgrd = 1
    elif grd > 4 and grd <= 11 :
        rgrd = 2
    elif grd > 11 and grd <= 23 :
        rgrd = 3
    elif grd > 23 and grd <= 40 :
        rgrd = 4
    elif grd > 40 and grd <= 60 :
        rgrd = 5
    elif grd > 60 and grd <= 77 :
        rgrd = 6
    elif grd > 77 and grd <= 89 :
        rgrd = 7
    elif grd > 89 and grd <= 96 :
        rgrd = 8
    else :
        rgrd = 9

    return rgrd



n, k = map(int, sys.stdin.readline().rstrip().split())

li = list(map(int, sys.stdin.readline().rstrip().split()))

for x in li :
    print(grade(x), end=" ")