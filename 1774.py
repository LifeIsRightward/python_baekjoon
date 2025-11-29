import sys
sys.setrecursionlimit(10**7)

def distance(x1, x2, y1, y2) :
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

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
    
def check_cycle(x, y) :
    return find_root(x) == find_root(y)


v, linked_num = map(int, sys.stdin.readline().rstrip().split())

nodes = []

for i in range(1, v+1) :
    x_pos, y_pos = map(int,sys.stdin.readline().rstrip().split())
    #정점 정보 담아두기(정점 번호, x좌표, y좌표)
    # 예를 들어 몇 번 별. 느낌인거임 i 는
    nodes.append((i, x_pos, y_pos))

root_node = []

for i in range(v+1) :
    root_node.append(i)


edges = []

# 간선 정보 만들어주기
for nodenunm1, x1, y1 in nodes :
    for nodenum2, x2, y2 in nodes:
        edges.append((nodenunm1, nodenum2, distance(x1, x2, y1, y2)))

edges.sort(key=lambda x: x[2])


# 이미 연결되어있는 통로는 그냥 Union 시키면됨. (cost를 고려할 필요가 없음, 이미 연결된건 cost가 0인거임)
# 이미 설치된 도로라고 생각하면됨. 추가로 설치해야 할 도로의 cost만을 고려해야하기 때문.
for _ in range(linked_num) :
    linked_x_pos, linked_y_pos = map(int, sys.stdin.readline().rstrip().split())
    union(linked_x_pos, linked_y_pos)

total_cost = 0

for x, y, cost in edges :
    if not check_cycle(x, y) :
        union(x, y)
        total_cost += cost

print(f'{total_cost:.2f}')

