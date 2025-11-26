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

def check_cycle(x, y) :
    return find_root(x) == find_root(y)


v, e = map(int, sys.stdin.readline().rstrip().split())

root_node = []

for i in range(v+1) :
    root_node.append(i)

edges = []

for i in range(e) :
    x, y, cost = map(int, sys.stdin.readline().rstrip().split())
    edges.append((x, y, cost, i+1))


edges.sort(key=lambda x: x[2])

vertexlist = []
edge_index_list = []

for x, y, cost, edge_index in edges :
    if not check_cycle(x,y) :
        union(x,y)
        if x not in vertexlist :
            vertexlist.append(x)
        if y not in vertexlist :
            vertexlist.append(y)

        edge_index_list.append(edge_index)

print(len(vertexlist)-1)
for edge_number in edge_index_list :
    print(edge_number)

