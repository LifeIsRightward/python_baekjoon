import sys
sys.setrecursionlimit(10**7)

def find_root(x) :
    if x == root_node[x] :
        return root_node[x]

    root_node[x] = find_root(root_node[x])
    return root_node[x]

def union(x, y) :
    x = find_root(x)
    y = find_root(y)

    if x != y :
        root_node[y] = x

# trye -> 사이클 발생. union 진행 불가
def chcek_cycle(x, y) :
    return find_root(x) == find_root(y)

def check_connected(v) :
    base = int(find_root(1))
    
    for x in range(1, v+1) :
        if base != find_root(x) :
            return False

    return True
    

# 정점, 간선
v, e = map(int, sys.stdin.readline().rstrip().split())

root_node = []

# root_node 초기화
for i in range(v+1) :
    root_node.append(i)

edges = []

for _ in range(e) :
    x, y, cost = map(int, sys.stdin.readline().rstrip().split())
    # 간선 정보 입력받기
    edges.append((x, y, cost))

# 그리디를 위한 정렬 -> 근데, 이 문제에서는 최대값을 구해야하니까 정렬을 내림차순으로하는게 맞을듯
edges.sort(key=lambda x : x[2], reverse=True)

total_cost = 0

for x, y, cost in edges :
    if not chcek_cycle(x, y) :
        union(x, y)
        total_cost += cost

if not check_connected(v) :
    print(-1)
else :
    print(total_cost)