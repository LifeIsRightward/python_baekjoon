import sys

n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))

li2 = li

li2.sort()

if li2 != li :
    print("0")
else :
    if len(li) == len(set(li)) : 
        print("1")
    else :
        print("0")






         