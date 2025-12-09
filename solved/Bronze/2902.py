import sys

ooo = []

ooo = sys.stdin.readline().rstrip().split('-')
result = []

for x in ooo :
     result.append(x[0])

for x in result :
     print(x, end='')