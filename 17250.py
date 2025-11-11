import sys
sys.setrecursionlimit(100000000)

def find_root(x) :
    if x == root_node[x] :
        return x
    else :
        root_node[x] = find_root(root_node[x])
        return root_node[x]


def union(x, y) :
    x = find_root(x)
    y = find_root(y)

    if x != y :
        # 합쳐진 각 노드의 행성개수는 공유된다. (각 은하 노드에)
        combined_galaxy = galaxy_node[x] + galaxy_node[y]
        # print(f'x: {galaxy_node[x]} | y: {galaxy_node[y]}')
        galaxy_node[x] = combined_galaxy
        galaxy_node[y] = combined_galaxy
        root_node[x] = y
        return combined_galaxy
    else :
        # 같아도 return은 해줘야하니까 필요함.
        # 그래서 galaxy_node[]를 x를 해줘도되고 y를 해줘도 상관없음. 이미 같은 그룹에 속해있어서 x든 y든 누가 리턴되어도 값은 똑같음.
        combined_galaxy = galaxy_node[x]
        return combined_galaxy


galaxy, subwayline = map(int, sys.stdin.readline().rstrip().split())

# initial
# 각 은하의 노드 개수만큼 그 각각의 은하 노드의 부모는 자신이 될 것이다.
root_node = list(range(galaxy))

# 실제 값을 받아야 함. (은하 하나에 존재하는 행성 수)
galaxy_node = []


for _ in range(galaxy) :
    # 각 은하에 존재하는 행성들의 수를 입력받음.
    galaxy_node.append(int(sys.stdin.readline().rstrip()))

for _ in range(subwayline) :
    # 은하와 은하 사이 연결된 철도를 입력받기 위함.
    a, b = map(int, sys.stdin.readline().rstrip().split())

    # 입력받는 행성 번호가 1부터 시작이기에 Index out of range 오류가 발생함.
    print(union(a-1,b-1))
