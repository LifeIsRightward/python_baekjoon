import sys

class queue :
    def __init__(self):
        # queue라고 생각하자.
        self.arr = []

    def push(self, x):
        self.arr.append(x)

    def pop(self):
        if len(self.arr) == 0 : 
            return -1
        else :
            return self.arr.pop(0)

    def size(self):
        return len(self.arr)

    def empty(self):
        if len(self.arr) == 0 :
            return 1
        else :
            return 0
        
    def front(self) :
        if len(self.arr) == 0 :
            return -1
        else :
            return self.arr[0]
        
    def back(self) :
        if len(self.arr) == 0 :
            return -1
        else :
            return self.arr[-1]

n = int(input())

que = queue()

for i in range(n) :
    parts = list(sys.stdin.readline().rstrip().split())
    cmd = parts[0]

    if cmd == "push" : 
        val = parts[1]
        que.push(val)
    elif cmd == "pop" :
        print(que.pop())
    elif cmd == "size" :
        print(que.size())
    elif cmd == "empty" :
        print(que.empty())
    elif cmd == "front" : 
        print(que.front())
    elif cmd == "back" :
        print(que.back())



    