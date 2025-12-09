import sys

# 문제 -> 공부 시간의 한계를 초과하지 않으면서, 과목의 중요도 합이 최대인
# n은 최대 공부시간 | k는 과목 수
n, k = map(int, sys.stdin.readline().rstrip().split())

# k줄에 걸처서 중요도 cost 와 공부시간 time이 입력됨.

# dp table init
# 0값으로 n+1 개 만듦 -> 1차원 리스트
# 그걸 k번 반복 -> 2차원 리스트
# 즉, n x k 행렬이 만들어지는 셈.
# 리스트 컴프리헨션(for을 통한 초기화)을 사용하지 않고, [[0]*(n+1)] * k -> 이런식으로 dp 테이블을 초기화하게되면
# 얕은 복사 문제가 발생한다. -> 처음 만들어지는 dp[0][1] 값을 바꾸려고 해도, dp[1][1] 값도 달라진다는 거임.
# dp[1]이 dp[0]을 참조하고 있기 때문이다 -> 이 문제가 얕은 복사 (참조에 의한)
# dp = [[0]*(n+1) for _ in range(k)]
# 근데 이 문제는 이렇게 풀 이유가 없음.

# dp[t] = cost -> i시간에 뽑아내는 최대 효율 cost
# 총 공부시간 t 안에서 얻을 수 있는 최대 중요도 합
# t = 0 ~ n(n은 공부시간임)
# 예를들어 dp[3] = 5 는, 공부시간 3시간 안에 최대 충요도의 합이 5라는 뜻임.
dp = [0] * (n+1)


items = []

for _ in range(k) :
    cost, time = map(int, sys.stdin.readline().rstrip().split())
    items.append((cost, time))

# 각 과목을 순회하면서
for cost, time in items :
    # 시간 역순으로 순회 -> 같은 과목 선택 방지를 위함
    for t in range(n, time-1, -1) :
        dp[t] = max(dp[t], dp[t-time] + cost)
 
 
print(dp[n])
