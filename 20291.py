import sys

# 파일 개수 N
n = int(sys.stdin.readline().rstrip())

# {} -> 이건 딕셔너리임.
extension_name = {}


for _ in range(n) :
    name, extension = sys.stdin.readline().rstrip().split(".")
    
    if extension not in extension_name :
        extension_name[extension] = 1
    else :
        extension_name[extension] += 1
    

# 딕셔너리를 sorting 하면 튜플로 이루어진 list를 반환한다.
# key: value에서 Key를 기준으로 오름차순 정렬
sorted_dict = dict(sorted(extension_name.items()))

# 내가 딕셔너리 구조를 잘 몰라서... 공부해야할 듯
for key, value in sorted_dict.items() :
    print(f'{key} {value}')  