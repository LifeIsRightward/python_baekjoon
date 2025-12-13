import sys

n = int(sys.stdin.readline().rstrip())

std = []
for _ in range(n) :
    std.append(sys.stdin.readline().rstrip())

aws = []
for _ in range(n) :
    aws.append(sys.stdin.readline().rstrip())

total = 0
for i in range(n) :
    if std[i] == aws[i] :
        total += 1

print(total)
