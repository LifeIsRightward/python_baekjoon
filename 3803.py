import sys
sys.setrecursionlimit(10**5)

def find_root(x):
    if root_node[x] == x:
        return x
    root_node[x] = find_root(root_node[x])
    return root_node[x]

def union(x, y):
    x = find_root(x)
    y = find_root(y)
    if x != y:
        root_node[y] = x

def check_cycle(x, y):
    return find_root(x) == find_root(y)

while True:
    line = sys.stdin.readline()
    if not line:
        break

    line = line.strip()
    if line == "":
        continue

    if line == "0":
        break

    data = line.split()
    if len(data) != 2:
        continue

    v, e = map(int, data)

    root_node = [i for i in range(v + 1)]

    edges = []
    for _ in range(e):
        x, y, cost = map(int, sys.stdin.readline().split())
        edges.append((x, y, cost))

    edges.sort(key=lambda t: t[2])

    total_cost = 0
    for x, y, cost in edges:
        if not check_cycle(x, y):
            union(x, y)
            total_cost += cost

    print(total_cost)
