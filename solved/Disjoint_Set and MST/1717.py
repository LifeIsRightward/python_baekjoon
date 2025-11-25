import sys

sys.setrecursionlimit(100000000)

# n: 집합 수 (n+1개의 집합)
# m: 연산수 (union, find)
n, m = map(int, sys.stdin.readline().rstrip().split())

node = []
root = []

# 노드의 루트를 찾는 메서드(find)
def find_root(x) :
    # 내 노드가 곧 루트라면 -> 바로 return
    if x == root[x] :
        return x
    else :
        # 내 노드는 루트가 아니다. -> 찾으로 재귀로 들어감.
        # 재귀 다 마치고(내 루트를 찾았고) 루트 찾으러 가던 길에 있었던 녀석들의 루트 또한 지금 방금 막 찾은 노드이기 때문에
        # 재귀 돌아오면서 싹 다 root를 설정해줌.
        # 그니까, 맨 밑에 있던놈이 위로 올라 올라 가는게 재귀를 타는 현상인거고, 걔네들은 지금 루트의 자식들이니까.. 루트 설정을 해준다는 거임.
        # 이게 경로 압축이다.
        # 맨 밑에 있던놈이 또 밑에서 부터 타고 타고 올라가는게 아닌, 내 바로 위에 있는 놈의 root만 알아내면.. 한 번 만에 루트를 알 수 있으니까.
        root[x] = find_root(root[x])
        return root[x]


def union(x, y):
    x = find_root(x)
    y = find_root(y)

    if(x != y) : 
        root[x] = y


# 각 노드에 데이터 추가와 동시에 자기 자신이 root로 초기화 시키기.
for i in range(n+1):
    node.append(i)
    root.append(i)

for _ in range(m) :
    order, x, y = map(int, sys.stdin.readline().rstrip().split())

    if order == 0:
        union(x, y)
    else :
        if find_root(x) == find_root(y) :
            print("YES")
        else :
            print("NO")