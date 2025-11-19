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

# True를 반환한다면 -> 사이클이 생긴다는것 (부모가 같으니까)
def check_cycle(x, y) :
    return find_root(x) == find_root(y)


# 정점 (컴퓨터)
v = int(sys.stdin.readline().rstrip())

# 간선
e = int(sys.stdin.readline().rstrip())

# 정점의 부모노드 리스트 -> 초기화는 스스로가 부모
root = []

# 간선의 정보 (정점 1, 정점 2, 가중치)
edges = []

# 부모노드 리스트 초기화 (0번 인덱스 버림)
for i in range(v+1) :
    root.append(i)

# 간선정보
for _ in range(e) :
    x, y, cost = map(int, sys.stdin.readline().rstrip().split())
    # 튜플로 만들어서 List에 집어넣기
    edges.append((x, y, cost))

# 리스트 안에 있는 튜플 중 2번째 인덱스. 즉, cost를 기준으로 sort
# 이는 크루스칼에서 그리디를 위해 정렬함.
edges.sort(key= lambda t: t[2])

total_cost = 0

for x, y, cost in edges :
    # 사이클이 생기지 않는다면
    if not check_cycle(x, y) :
        union(x, y)
        total_cost += cost


print(total_cost)