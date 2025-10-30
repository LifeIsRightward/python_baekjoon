import sys

n = int(sys.stdin.readline())

arr = []

for i in range(n) :
    arr.append(int(sys.stdin.readline()))

arr.sort()
arr.reverse()

# list 길이는 len(list) 이렇게 쓰면 될듯.
for i in range(len(arr)) :
    print(arr[i])