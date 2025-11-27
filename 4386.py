import sys
sys.setrecursionlimit(10**7)

def distance(x1, x2, y1, y2) :
    return (((x2-x1)**2) + ((y2-y1)**2))**0.5


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


# 별 개수 입력 받기
v = int(sys.stdin.readline().rstrip())

stars_cordinate = []
root_node = []

for i in range(1, v+1) :
    x_position, y_position = map(float, sys.stdin.readline().rstrip().split())
    # 별 좌표 정보 받기
    # 거기에 별 순서를 달아줌 (i)
    stars_cordinate.append((i, x_position, y_position))


# root_node는 어케 만들건데...? -> 내가 번호 1번부터 달아놨으니까 똑같이 만들면 되겠지 뭐
for i in range(v+1) :
    root_node.append(i)

edges = []

# 간선 정보 만들기 (x, y, cost) 예를 들어 (1, 2, 100) 사실 루프를 만들어도 어짜피 mst에서 선택 안받아서 상관 없을 듯
for star_num1, x1, y1 in stars_cordinate :
    for star_num2, x2, y2 in stars_cordinate :
        edges.append((star_num1, star_num2, distance(x1, x2, y1, y2)))

edges.sort(key=lambda x: x[2])

total_cost = 0

for x, y, cost in edges :
    if not check_cycle(x, y) :
        union(x, y)
        total_cost += cost

print(f'{total_cost:.2f}')


