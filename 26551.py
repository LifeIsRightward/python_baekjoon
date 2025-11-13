import sys
sys.setrecursionlimit(100000000)

node = []
root_node = []

# 인덱스를 파람으로 집어넣자
def find_root(x) :
    # x라는 이름의 사람이 존재하는 node의 idx -> 얘는 node, root_node가 Mapping 됨 (이니셜라이징을 그렇게 해놨기 때문.)
    # 어떤 사람의 이름이 있는 node의 인덱스랑 == root_node[그 사람 노드 인덱스 값] (즉, 매핑되니까 같으면)
    # 내가 내 부모라는거임
    if x == root_node[x] :
        return root_node[x]
    
    # 내가 내 스스로 부모가 아니고, 누군가가 부모니까, 지금 내 부모(내가 아닌 누군가)의 부모를 찾으로 또 들어감.
    root_node[x] = find_root(root_node[x])

    # 그리고 재귀가 마지막에 끝나고 복귀할 때 root_node[x] 값을 리턴하면서 위의 구문에 대입시켜주면서 복귀됨
    return root_node[x]


def union(x, y) :
    x = find_root(x)
    y = find_root(y)

    # 연결 시키기
    if x!=y :
        root_node[y] = x

        
def check_connection(x, y) :
    x = find_root(x)
    y = find_root(y)

    if x != y :
        return False
        
    else :
        return True
        

# 이름 연결(가족 구성) 이름
n = int(sys.stdin.readline().rstrip())

# 정보 입력받기 및 관계(연결) 설정
for i in range(n) :
    # a: 이름, b: 관계, c: 이름
    a, b, c = sys.stdin.readline().rstrip().split()
    
    # 만약 새로 받은 정보라면 집어넣고 아니면 그냥 아무일도 없게 처리
    # 이 때, 노드랑 노드의 부모를 self로 initial 해놓기
    
    if not(a in node) :
        node.append(a)
        root_node.append(len(root_node))


    if not(c in node) :
        node.append(c)
        root_node.append(len(root_node))

    a_idx = node.index(a)
    c_idx = node.index(c)



    # 그리고 관계 연결하기
    # Error -> list의 인덱스를 string으로 사용하면
    # TypeError: list indices must be integers or slices, not str 오류가 발생함.
    # 그럼, 입력값에 해당하는 List의 index를 반환받아서 사용해야 될 듯 하다.

    # 그 노드의 인덱스를 넣어보자.
    union(a_idx, c_idx)

# 확인 TC
m = int(sys.stdin.readline().rstrip())

for _ in range(m) :
    p1, p2 = sys.stdin.readline().rstrip().split()

    p1_idx = node.index(p1)
    p2_idx = node.index(p2)

    if check_connection(p1_idx, p2_idx) :
        print("Related")
    else :
        print("Not Related")