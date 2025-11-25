import sys
sys.setrecursionlimit(1000000)

def find_root(x) : 
    if root[x] == x :
        return root[x]
    
    # 내(x) 부모의(root[x]) 부모를 찾아줘, 그리고 재귀돌면서 값 찾고 돌아오면서 대입 빠빠박 -> 경로 압축
    root[x] = find_root(root[x])
    return root[x]


def union(x, y) :
    x = find_root(x)
    y = find_root(y)

    if x != y :
        root[y] = x


def check_cycle(x, y) :
    return find_root(x) == find_root(y)



# 정점 v, 간선 e
v, e = map(int, sys.stdin.readline().rstrip().split())

# 부모 노드 초기화
root = []
for i in range(v+1) :
    root.append(i)

# 간선의 정보
edges = []

# 간선 정보 입력받아서 저장
for _ in range(e) :
    x, y, cost = map(int, sys.stdin.readline().rstrip().split())
    edges.append((x, y, cost))

# 정렬 -> 그리디를 위함 (앞에서부터 cost가 낮을테니 순회하면 됨)
# 근데 sort 파라미터 key.. 이거랑, lambda 이거 잘 모르겠다.
edges.sort(key= lambda t: t[2])

total_cost = 0
mst = []

# 두 개의 마을로 분리할 때, 최소 마을 하나에 하나의 집이 있어야 함.
# 그렇다면, 기존 Mst에서 가장 가중치가 큰 간선을 제거한다면
# 가장 낮은 비용으로 두 마을을 분리하여 운영할 수 있게됨.

for x, y, cost in edges :
    if not check_cycle(x, y) :
        # print(f'x: {x}, y: {y}, cost: {cost}')
        union(x, y)
        mst.append((x, y, cost))

# 맨 마지막 간선 (가중치가 가장 높은 간선의 정보 pop)
mst.pop()

for x, y, cost in mst :
    total_cost += cost

print(total_cost)

