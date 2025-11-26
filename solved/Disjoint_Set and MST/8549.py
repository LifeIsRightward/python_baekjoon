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

for i in range (v+1) :
    root_node.append(i)

edges = []

for _ in range(e) :
    x, y, cost = map(int, sys.stdin.readline().rstrip().split())
    edges.append((x, y, cost))

edges.sort(key=lambda x: x[2])

costlist = []

for x, y, cost in edges :
    if not check_cycle(x, y) :
        union(x,y)
        costlist.append(cost)

costlist.sort(reverse=True)
print(costlist[0])
