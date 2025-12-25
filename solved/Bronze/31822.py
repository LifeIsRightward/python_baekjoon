import sys

target = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())

qqq = []

for _ in range(n) :
    qqq.append(sys.stdin.readline().rstrip())


for _ in range(n):
    qqq.append(sys.stdin.readline().rstrip())

count = 0

for code in qqq:
    if code[:5] == target[:5]:   # 앞 5글자 비교
        count += 1

print(count)