from collections import deque
import sys


def process():
      for cmd in p:
          if cmd == 'D':
              if len(arr) == 0:
                  print("error")
                  return  # 함수 종료 = 다음 테스트 케이스로
              else:
                  arr.popleft()
          elif cmd == 'R':
              reversed(arr)

      print(list(arr))

# 전체 테스트 케이스 수
tc = int(sys.stdin.readline())

for _ in range(tc):
    p = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    arr_str = sys.stdin.readline().strip()

    # 배열이 비어있는 경우 예외처리
    if arr_str == "[]":
        arr = deque()
    else:
        arr = deque(map(int, arr_str[1:-1].split(',')))

    process()