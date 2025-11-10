import sys
sys.setrecursionlimit(100000000)

def find_root(x) :
    if x == root_node[x] :
        return x
    else :
        root_node[x] = find_root(root_node[x])
        return root_node[x]


def union(x, y) :
    x = find_root[x]
    y = find_root[y]

    if x != y :
        # 합쳐진 각 노드의 행성개수는 공유된다. (각 은하 노드에)
        combined_galaxy = galaxy_node[x] + galaxy_node[y]
        galaxy_node[x] = combined_galaxy
        galaxy_node[y] = combined_galaxy
        root_node[x] = y
        return combined_galaxy 

galaxy, subwayline = map(int, sys.stdin.readline().rstrip().split())

# initial
root_node = list(range(galaxy))
# 실제 값을 받아야 함. (은하 하나에 존재하는 행성 수)
galaxy_node = []

for _ in range(galaxy) :
    galaxy_node.append(int(sys.stdin.readline().rstrip().split()))