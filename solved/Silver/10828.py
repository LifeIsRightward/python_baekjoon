import sys


class stack :
    def __init__(self):
        # stack이라 생각하자.
        self.arr = []
        
    def push(self, x) :
        self.arr.append(x)

    def pop(self) : 
        if len(self.arr) == 0:
            return -1
        else :
            return self.arr.pop()
        
    def size(self) :
        return len(self.arr)
    
    def empty(self) :
        if len(self.arr) == 0 :
            return 1
        else :
            return 0
        
    def top(self) : 
        if len(self.arr) == 0 :
            return -1
        else : 
            # 인덱스를 음수로도 표현할 수 있음. 맨 뒤가 -1임.
            return self.arr[-1]

attempt = int(input())

stk = stack()

for i in range(attempt) :
    parts = sys.stdin.readline().rstrip().split()
    cmd = parts[0]
    
    if cmd == "push" :
        n = int(parts[1])
        stk.push(n)
    elif cmd == "top" :
        print(stk.top())
    elif cmd == "size" :
        print(stk.size())
    elif cmd == "empty" :
        print(stk.empty())
    elif cmd == "pop" :
        print(stk.pop())
    




