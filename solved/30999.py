import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
cnt = 0

for i in range(n) :
    # 붙어서 입력이 들어오는 경우에는 굳이 split() 할 필요없이 list로만 해주면 한 글자 씩 끊어준다.
    arr = list(sys.stdin.readline().strip())
    approved = arr.count("O")
    rejected = arr.count("X")

    if approved > rejected :
        cnt += 1

print(cnt)