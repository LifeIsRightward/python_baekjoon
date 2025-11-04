import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

# deque 선언할 때, 생성자처럼 해줘야 함.
originqueue = deque()
answerlist = deque()

# print(f"{n}, {k}")
# init queue
# 1부터 n까지 들어가려면 n+1 해줘야함
for i in range(1, n+1) :
    # print(i)
    originqueue.append(i)

# print(f"len: {len(originqueue)}")

for j in range(len(originqueue)) :
    # print(f"{j}")
    for inner in range(k):
        if inner == k-1 :
            answerlist.append(originqueue.popleft())
        else :
            originqueue.append(originqueue.popleft())

# print("===================================")

print("<", end="")
for tmp in range(len(answerlist)-1) :
    print(answerlist.popleft(), end=", ")
print(answerlist.popleft(), end="")
print(">", end="")
