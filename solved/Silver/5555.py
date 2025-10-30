import sys

#rstrip()안썻거 문제가 생겼었음. 입력받은 문자열에서, 찾고싶은 특정 문자열을 찾는 문제였다.
# 내가 입력받은 문자열은, 순수 내가 입력한 문자열이 아닌, 개행(엔터)가 들어간 문자열임.
# 그래서 못찾았던거임... 항상 비교를 엔터들어간 녀석들끼리 했으니까
str = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())

cnt = 0

for i in range(n) :
    tmpstr = sys.stdin.readline().rstrip()
    
    # 반지는 둥그니까 순환가능.. 적어도 두 번은 싸이클을 돌려야 보일거같음.
    tmpstr = tmpstr*2
    tmpjudgeval = tmpstr.find(str)

    #print(tmpjudgeval)
    
    if(tmpjudgeval != -1) :
        cnt += 1

print(cnt)