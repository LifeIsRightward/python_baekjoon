import sys
sys.setrecursionlimit(10000000)

# 섬 개수
n = int(sys.stdin.readline().rstrip())

node = []
root_node = []

def find_root(x) :
    if root_node[x] == x :
        return root_node[x]
    
    # 내 부모의 루트를 찾겠다. 그걸 재귀 풀리고 돌아오면서 대입하는거고
    root_node[x] = find_root(root_node[x])
    return root_node[x]

def union(x, y) :
    x = find_root(x)
    y = find_root(y)

    if x != y :
        root_node[y] = x

def pick_node() :
    # 맨 앞에 루트 노드가 기준이라고 내 맘대로 설정함. (아무거나 루트가 다른 두 섬을 고르면 되니까)
    standard = find_root(0)

    for i in range(1, n) :
        if standard != find_root(i) :
            # standard랑 다른놈 찾음
            return [0, i]

    
# initializing (node - root_node mapping)
for i in range(n) :
    node.append(i)
    root_node.append(i)

# 연결된 섬과섬 정보
for _ in range(n-2) :
    x, y = map(int, sys.stdin.readline().rstrip().split())

    union(x-1, y-1)

a, b = map(int, pick_node())

print(f'{a+1} {b+1}')

