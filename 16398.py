import sys
sys.setrecursionlimit(10**7)

def find_root(x) :
    if root_node[x] == x :
        return root_node[x]
    
    root_node[x] = find_root(root_node[x])
    return root_node[x]

def union(x, y) :
    x = find_root(x)
    y = find_root(y)

    if x != y :
        root_node[y] = x

def check_cycle(x, y) :
    return find_root(x) == find_root(y)


v = int(sys.stdin.readline().rstrip())

root_node = []

for i in range(v+1) :
    root_node.append(i)

cost = []
# 일단 cost 입력 받기
for _ in range (v) :
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    cost.append(row)

edges = []
# cost + 좌표를 통한 edges 정보 만들기 (간선 정보 만들기)
for x in range (1, v+1) :
    for y in range (1, v+1) :
        edges.append((x, y, cost[x-1][y-1]))

edges.sort(key=lambda x: x[2])

total_cost = 0
for x, y, cost in edges :
    if not check_cycle(x, y) :
        union(x, y)
        total_cost += cost

print(total_cost)



