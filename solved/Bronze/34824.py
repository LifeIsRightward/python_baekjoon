import sys

n = int(sys.stdin.readline().rstrip())

aaa = []

for _ in range(n) :
    aaa.append(sys.stdin.readline().rstrip())

y = aaa.index("yonsei")
k = aaa.index("korea")

if (y < k) :
    print('Yonsei Won!')
else :
    print("Yonsei Lost...")
