import sys
sys.setrecursionlimit(1000000)

def find_root(x) :
    if root[x] == x :
        return root[x]
    
    # 내(x) 부모(root[x])의 루트를 찾아줘
    root[x] = find_root(root[x])
    return root[x]

def union(x, y) :
    x = find_root(x)
    y = find_root(y)

    if x != y :
        root[y] = x

# mst를 그리디로 진행할 때, 연결해도 괜찮은지를 확인하는 메서드 (사이클이 생기는지에 대한 유무 체킹)
# x, y 정점의 실제 부모를 불러와 놓고, 이미 같은 부모라면 어케든 연결이 되어있다는건데
# 여기서 또 연결하버리면 -> 사이클이 발생한다는 뜻
# True 반환은 -> 사이클이 생김.
# False 반환은 -> 사이클이 안생김.
def check_cycle(x, y) :
    return find_root(x) == find_root(y)


# 도사 개수, 도로 개수, 정복할 때 마다 증가하는 도로의 비용
v, e, default_cost = map(int, sys.stdin.readline().rstrip().split())

# 정점의 부모 리스트
root = []

# 부모 리스트 초기화 (0번 인덱스는 버림. 1번 인덱스부터 사용할거)
for i in range(v+1) :
    root.append(i)

# 간선 정보들
edges = []

# 간선 정보 받기
for _ in range(e) :
    x, y, cost = map(int, sys.stdin.readline().rstrip().split())
    # 간선 정보 리스트에 튜플로 추가
    edges.append((x, y, cost))

# 그리디를 위한 cost중심 정렬
edges.sort(key= lambda t: t[2])

total_cost = 0
cnt = 0

for x, y, cost in edges :
    if not check_cycle(x, y) :
        union(x, y)
        total_cost += cost + (default_cost * cnt)
        cnt += 1

print(total_cost)

