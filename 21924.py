import sys
sys.setrecursionlimit(10000000)

# find
def find_root(x) :
    if root[x] == x :
        return root[x]
    
    root[x] = find_root(root[x])
    return root[x]

# union
def union(x, y) :
    x = find_root(x)
    y = find_root(y)

    if x != y :
        root[y] = x

# cycle checking
def check_cycle(x, y) :
    return find_root(x) == find_root(y)


# 전체 간선 정보, mst 간선 정보가 파라미터에 들어감.
# 그럼 전체 간선 정보의 토탈 cost와
# 실제로 만들어진 mst의 cost를 얻기 위한 메서드
def check_all_cost(edgeslist) :
    total_cost = 0
    for x, y, cost in edgeslist :
        total_cost += cost

    return total_cost


# 연결 안되어있는지 확인
def check_disconnected(rootlist) :
    # 1번 점점에 대해서 루트 탐색.
    # 이를 기준으로 삼는다.
    base = find_root(1)

    # i는 1부터 rootlist까지
    # 돌아가면서 i번 노드를 find_root로 찾아보고
    # 만약 기준인 base와 다르다면
    # disconnected 되어있다고 True 반환
    for i in range(1, len(rootlist)) :
        if find_root(i) != base :
            return True
    
    return False


# v: 정점, e: 간선

v, e = map(int, sys.stdin.readline().rstrip().split())

# 부모 리스트
root =[]

# 간선 정보
edges = []

# 부모 리스트 초기화
for i in range(v+1) :
    root.append(i)

# 간선 정보 입력받기
for _ in range(e) :
    x, y, cost = map(int, sys.stdin.readline().rstrip().split())
    edges.append((x, y, cost))

# 그리디를 위한 정렬
edges.sort(key= lambda t: t[2])

mstinfo = []

for x, y, cost in edges :
    if not check_cycle(x, y) :
        union(x, y)
        mstinfo.append((x, y, cost))


if check_disconnected(root) :
    print("-1")
else :
    total = check_all_cost(edges)
    mst = check_all_cost(mstinfo)
    print(total - mst)


