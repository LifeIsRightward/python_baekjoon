import sys

n = int(sys.stdin.readline().rstrip())

lev = map(int, sys.stdin.readline().rstrip().split())

for x in lev :
    if x == 300 :
        print("1", end=" ")
    elif x >= 275 and x < 300 :
        print("2", end=" ")
    elif x >= 250 and x < 275 :
        print("3", end=" ")
    else :
        print("4", end=" ")