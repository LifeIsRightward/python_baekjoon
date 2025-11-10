import sys
# 재귀 제한 풀기
sys.setrecursionlimit(100000000)


def find_root(x) :
    if x == root_node[x] :
        return x
    else :
        # 지금 들어온 내가 찾으려는 x가 루트노드가 아닐경우. (자기 자신이 루트노드가 아닐경우)
        # x는 현재 "나" 임.
        # 현재 파람으로 받은 나의 부모를 -> find_root(나의 부모). 즉, 내 부모의 부모를 찾아서 대입해놓겠다.
        root_node[x] = find_root(root_node[x])
        # 내 루트노드의 루트노드를 찾는다.
        return root_node[x]

def union(x, y) :
    x = find_root(x)
    y = find_root(y)

    if x != y :
        root_node[x] = y
        return False
    else :
        # 사실 같아도 연결하는게 큰 문제는 아님. 대신 이번 문제에서는 같게되면 사이클이 생기기에
        # flag를 처리하기 위한 구문이 필요했을 뿐.
        # 내가 연결하려는 놈이, 이미 나랑 같은 root면 -> Cycle이 생기는 거니까.
        root_node[x] = y 
        return True


amount, order = map(int, sys.stdin.readline().rstrip().split())

node = []
root_node = []

# 초기 정점 세팅 + 각 정점의 root는 자기 자신.
for i in range(amount) :
    node.append(i)
    root_node.append(i)

for j in range(order) :
    a, b = map(int, sys.stdin.readline().rstrip().split())

    if union(a, b) :
        print(j+1)
        break

# 끝 까지 다 돌았음에도 Cycle이 없었다.. -> 0 출력 처리
# for랑 while도 else랑 매칭이되는걸로 나오네
# for나 while에서 break가 한 번도 안나오면 else 실행이라네
else :
    print("0")