import sys

# 걍 느낀건, input()은 개행을 떼고 리턴해줌.
# sys.stdin.readline()은 개행문자 달고 속 시원하게 걍 리턴해줌
# 아마 그런 하나의 태스크 차이 때문에 속도가 차이난다고 이야기하는 것 같은데, 그게 실제로 얼마나 차이날까 싶기도 하고
# sys.stdin.readline() 하면 결과가 Print로 찍었을때 "\n" 요거 나옴
# 그래서 뒤에 rstrip() 붙여주는거임.
# 더 찾아보긴 해야할 듯?

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)