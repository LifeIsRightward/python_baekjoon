import sys
sys.setrecursionlimit(10000000)


def init() :
    # 정점개수, 간선개수
    v, e = map(int, sys.stdin.readline().rstrip().split())

    # 정점의 부모 저장 리스트
    root_node = []
    
    # 정점의 부모 초기화
    for i in range(v+1):
        root_node.append(i)

    # 간선 정보 저장 리스트
    edges = []

    # 간선 정보 저장
    for _ in range(e) :
        x, y, cost = map(int, sys.stdin.readline().rstrip().split())
        edges.append((x, y, cost))

    return root_node, edges



def find_root(root_node, x) :
    if x == root_node[x] :
        return root_node[x]

    root_node[x] = find_root(root_node, root_node[x])
    return root_node[x]

def union(root_node, x, y) :
    x = find_root(root_node, x)
    y = find_root(root_node, y)

    if x != y :
        root_node[y] = x

# true 이면 -> cycle이 있다는 이야기.
# 즉, 합치면 안됨.
def check_cycle(root_node, x, y): 
    return find_root(root_node, x) == find_root(root_node, y)

def solve(root_node, edges) :
    # 그리디를 위한 정렬
    edges.sort(key=lambda x: x[2])
    
    total_cost = 0

    for x, y, cost in edges :
        if not check_cycle(root_node, x, y) :
            union(root_node, x, y)
            total_cost += cost

    return total_cost


# Testcase
tc = int(sys.stdin.readline().rstrip())

for i in range(1, tc+1) :
    # 언패킹
    cost = int(solve(*init()))
    print(f'Case #{i}: {cost} meters')

