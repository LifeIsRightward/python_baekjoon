import sys

class stack :
    def __init__(self):
        self.stk = []
        self.undostk = []

    def push(self, i) :
        self.stk.append(i)
        self.undostk.append(["push", i])
    def pop(self) :
        popval = self.stk.pop()
        self.undostk.append(["pop", popval])
    def undo(self) : 
        tmplist = self.undostk.pop()
        cmd = tmplist[0]
        val = tmplist[1]

        if(cmd == "push") :
            self.stk.pop()
        elif(cmd == "pop") :
            self.stk.append(val)
    def size(self) :
        return len(self.stk)
    def top(self) :
        if len(self.stk) == 0 :
            return -1
        else :
            return self.stk[-1]


# 쿼리 입력받기
query = int(sys.stdin.readline().rstrip())

stk = stack()


for q in range(query) :
    parts = list(sys.stdin.readline().split())
    cmd = parts[0]

    if cmd == "1" :
        val = int(parts[1])
        stk.push(val)
    elif cmd == "2" :
       stk.pop()
    elif cmd == "3" :
        val = int(parts[1])

        for j in range(val) : 
            stk.undo()
    elif cmd == "4" :
        print(stk.size())
    elif cmd == "5" :
        print(stk.top())

'''
이해를 잘 못하겠어 나는 push, i라는 한 쌍을 리스트에 한 인덱스에 넣으려고 했던건데 왜 문제가 되는걸까 

⏺ 아, 이해했습니다! 설명해드리겠습니다.

  list()는 생성자 함수로, 이터러블 객체 하나를 받아서 리스트로 변환하는 역할을 합니다. 예를 들어:
  - list("abc") → ['a', 'b', 'c'] (문자열을 리스트로 변환)
  - list((1, 2, 3)) → [1, 2, 3] (튜플을 리스트로 변환)

  list()는 여러 개의 인자를 받을 수 없습니다. 그래서 list("push", i)처럼 2개의 인자를 전달하면 타입 에러가 발생합니다.

  당신이 원하는 것은 "push"와 i를 요소로 가진 새로운 리스트를 만드는 것이죠. 이럴 때는:

  1. 대괄호 [] 사용 (가장 일반적):
  self.undostk.append(["push", i])
  2. 또는 list() 안에 튜플을 넣기:
  self.undostk.append(list(("push", i)))

  하지만 첫 번째 방법(["push", i])이 훨씬 간단하고 파이썬에서 일반적으로 사용하는 방식입니다.

  정리하면:
  - list("push", i) ❌ - list()는 인자 2개를 받을 수 없음
  - ["push", i] ✅ - 두 요소를 가진 새 리스트 생성
'''