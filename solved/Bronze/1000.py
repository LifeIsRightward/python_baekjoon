#input()은 입력값을 받는 유일한 python 문법인가보다. 이는 string으로 값을 받는다.
# 하나의 문자열은 int()로 바꿀 수 있지만.. List는 그 안에들어있는 모든 문자열들, 단 한번의 int()로 전부 바꿀 수 없다.
# 따라서 map() 함수를 사용하여 list 각각의 원소에게 int()를 걸어줘야한다.
arr = list(map(int, input().split()))

print(arr[0] + arr[1])
