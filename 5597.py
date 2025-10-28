import sys

# 30까지 False로 init
# 방법1
arr = [False] * 30

# 30까지 False로 init
# 방법2
'''
for x in range(30) :
    arr.append(False)
'''

# 과제 제출 28명 True
for i in range(28) :
    arr[int(input())] = True

for y in range(30) :
    if arr[y] != True :
        print(arr[y]) 

