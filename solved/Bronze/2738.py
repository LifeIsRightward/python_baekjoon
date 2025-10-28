import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

a = []
b = []


# a 리스트 받는중
for i in range(n) :
    a.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
# b 리스트 받는중
# 근데 세로(n)에 대해서만 반복하고, 어짜피 m은 다 받고 split 할거니까 ㅇㅇ.
# 반복문 돌릴 이유가 없음.
for j in range(n) :
    b.append(list(map(int, sys.stdin.readline().rstrip().split())))


for i in range(n) :
    for j in range(m) :
        print(a[i][j] + b[i][j], end=" ")
    print()