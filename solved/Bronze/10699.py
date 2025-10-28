import datetime

# 첨에 str로 타입캐스팅 안해주고 했었는데 오류남. 아무래도 datetime.datetime.now()는 string을 반환하지 않나보다.
string = str(datetime.datetime.now())
arr = string.split()
print(arr[0])