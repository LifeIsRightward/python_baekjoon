import sys

# 나의 루트를 찾는거임. 진짜 내 부모 말고 내 위로 쭈욱 가다가 맨 처음이 루트.
def find(x) :
    if x == parent[x] :
        return parent[x]
    else :
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y) :
    x = find(x)
    y = find(y)
    
    # x, y 두 부모가 같지 않다면 -> 합쳐주는 과정을 진행
    if x != y :
        # y의 부모를, x의 최상단 부모랑 합쳐. 그럼 y도 x랑 부모가 같아지겠지
        parent[y] = x

def check(x, y) :
    x = find(x)
    y = find(y)

    if x != y :
        return False
    else :
        return True


# Test case
t = int(sys.stdin.readline().rstrip())

for i in range(t) :
    # user num
    n = int(sys.stdin.readline().rstrip())
    
    parent = []
    node = []
    

    # 부모, 노드 초기화
    for init in range(n+1) :
        parent.append(init)
        node.append(init)
    
    print(f"Scenario {i+1}:")
    k = int(sys.stdin.readline().rstrip())

    for j in range(k) :
        a, b = map(int, sys.stdin.readline().rstrip().split())
        union(a, b)

    m = int(sys.stdin.readline().rstrip())
    for _ in range(m) :
        x, y = map(int, sys.stdin.readline().rstrip().split())
        
        if check(x, y) :
            print("1")
        else :
            print("0")
    print()
    

