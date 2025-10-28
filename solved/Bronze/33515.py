# split()은, 문자열을 구분자로 자르는거임. -> return이 string array   
# int로 타입캐스팅 -> 앞에 (int) 이게 아니라, int로 묶음. int(arr[0])
# strcmp랑 다르게 같냐 다르냐를 보는게 아니라, 문자열 앞에서 부터 비교한다.
# 1 0 0 / 2 0 이면 | 1이랑 2비교 이렇게 그래서 20이 100보다 더 크다고 나온듯.
# 모르겠으면 if else에서 int 타입캐스팅 빼보고 돌려보셈 ㅇㅇ

string = input()
arr = string.split()
#print(arr[0], arr[1])

#print(min(arr[0], arr[1]))

if int(arr[0]) <= int(arr[1]) :
    print(arr[0])
else :
    print(arr[1])    
