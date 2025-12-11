import sys

team, have_chair, cost, transfee = map(int, sys.stdin.readline().rstrip().split())

remain = have_chair - (team * 3)

if remain >= 0 :
    print("0")
else :
    print(remain * -1 * cost + transfee)
