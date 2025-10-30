import sys

class stack :
    def __init__(self):
        self.stk = []
    
    def push(self, i) :
        self.stk.append(i)
    def pop(self) :
        self.stk.pop()
    #def undo(self, j) : 
        # undo 구현
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
        stk.push(int(parts[1]))
    elif cmd == "2" :
        stk.pop()
    elif cmd == "3" :
        print("Have to implement undo method")
    elif cmd == "4" :
        print(stk.size())
    elif cmd == "5" :
        print(stk.top())
