# 한 줄에 전부 입력받으면 한개 input()에 split()을 때리면 되는데.. 개행(엔터)가 있다면 여러번의 input()을 써야함.
# -> 어찌보면 당연한 이야기지 ㅇㅇ

x = int(input())
y = int(input())

if(x > 0 and y > 0):
    print("1")
elif (x > 0 and y < 0):
    print("4")
elif (x < 0 and y > 0):
    print("2")
elif (x < 0 and y < 0):
    print("3")