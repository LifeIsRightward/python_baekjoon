n = int(input())

  #end는 print()가 출력을 끝낸 후 마지막에 추가할 문자를 지정합니다.

  # 기본 형태 (생략 가능)
  #print("Hello", end="\n")  # 끝에 줄바꿈 추가 (기본값)

  # 줄바꿈 없이
  #print("Hello", end="")    # 끝에 아무것도 추가 안 함

for i in range(n): 
    for j in range(i+1): 
        # 한 줄에 여러 별을 찍으려면, print("*", end="")를 사용해야 한다.
        # 이것은 print()의 end 파라미터 기본값이 "\n" (줄 바꿈)이기 때문입니다.
        print("*", end="")
    print()

        
# 먼가 여기서 볼 점은, 내가 원하는 위치에 개행을 하기위한 for문 구분방법
# print의 end 인자값 디폴트는 개행이라는거.
# 그래서 일반적으로 print()하면 개행이 된다는 것. 이정도..?

'''
  n = int(input())

  for i in range(1, n+1):
      print("*" * i)
'''
# 이거는 좀 더 간단한 방법.
# 그리고 여러줄 주석은, 작은 따옴표 3개로 묶기
