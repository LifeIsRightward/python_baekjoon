import sys

# 31까지 False로 init -> 31까지 해야 인덱스가 30까지 갈테니까.
# 0부터 30까지의 인덱스 들을 False로 초기화한거임.
# 방법1
arr = [False] * 31

# 31까지 False로 init
# 방법2
'''
for x in range(31) :
    arr.append(False)
'''

# 과제 제출 28명 True
for i in range(28) :
    arr[int(input())] = True

for y in range(1, 31) :
    if arr[y] != True :
        print(y) 

