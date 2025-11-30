import sys
sys.setrecursionlimit(10**5)

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

# 부모가 같지 않다면 True를 return -> True이면 union을 진행하면 됨.
def check_cycle(x, y) :
    return find_root(x) != find_root(y)

# 성별이 다를 경우에만 이어질 수 있음. 성별이 다를 경우에 -> True를 retrun
def check_gender(x, y) :
    return gender_info_list[x] != gender_info_list[y]


def check_all_connected(v) :
    base = find_root(1)

    for i in range(2, v+1):
        if base != find_root(i) :
            return False
    return True


v, e = map(int, sys.stdin.readline().rstrip().split())

# 0번 버림.
gender_info_list = []
gender_info_list.append(None)
gender_value = sys.stdin.readline().rstrip().split()
gender_info_list.extend(gender_value)

# print(gender_info_list)

root_node = []
for i in range(v+1) :
    root_node.append(i)

edges = []
for _ in range(e) :
    x, y, cost = map(int, sys.stdin.readline().rstrip().split())
    edges.append((x, y, cost))

edges.sort(key=lambda t: t[2])

total_cost = 0
for x, y, cost in edges :
    if check_cycle(x, y) and check_gender(x, y) :
        union(x, y)
        total_cost += cost

if check_all_connected(v) :
    print(total_cost)
else :
    print("-1")