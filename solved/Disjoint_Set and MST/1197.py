import sys
sys.setrecursionlimit(1000000000)

def find_root(x) :
    if root[x] == x :
        return root[x]
    
    # 내가 부모가 아니라면, 내 부모(root[x])의 부모를 찾아줘
    root[x] = find_root(root[x])
    return root[x]


def union(x, y) :
    x = find_root(x)
    y = find_root(y)

    # 다르다면 합쳐주기
    if x != y :
        root[y] = x
    
    #뭐 같으면 암것도 안해줘도되니까.

# 간선 추가시, 사이클이 생기는지 확인
def check_cycle(x, y) :
    return find_root(x) == find_root(y)



# v는 정점, e는 간선
v, e = map(int, sys.stdin.readline().rstrip().split())

edges = []

# 각 정점의 루트 노드
root = []

# 부모 노드 초기화 -> 초기는 나 정점 스스로가 부모임.
# 0번 버리고 1번부터 V번째 인덱스까지 쓰기 위함
for i in range(v+1) :
    root.append(i)

# 간선정보 리스트 edges 입력받기
for _ in range(e) :
    x, y, w = map(int, sys.stdin.readline().rstrip().split())
    edges.append((x, y, w))

# sorting (파이썬 리스트 sort는 tema sort -> n log n)
# edges의 있는 튜플의 2번째 인덱스 정보(간선 가중치) 기준으로 정렬
edges.sort(key= lambda x: x[2])

weight = 0

for x, y, w in edges :

    # 내가 지금 연결하려는 x, y 정점이, 사이클이 발생할까? 에 대한 조건
    # 사이클이 발생하지 않는다면 -> True
    if not check_cycle(x, y) :
        union(x,y)
        weight += w

print(weight)