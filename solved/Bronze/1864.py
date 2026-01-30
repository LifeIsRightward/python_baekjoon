import sys

while True : 
    li = sys.stdin.readline().rstrip()

    if li[0] == "#" : 
        break
    else :
        total = 0
        for i in range(len(li)-1, -1, -1) :
             tmp = li[len(li)-1-i]
             trans = 0
             
             if tmp == "-" : 
                 trans = 0
             elif tmp == "\\" :
                 trans = 1
             elif tmp == "(" : 
                 trans = 2
             elif tmp == "@":
                 trans = 3
             elif tmp == "?" :
                 trans = 4
             elif tmp == ">" : 
                 trans = 5
             elif tmp == "&" :
                 trans = 6
             elif tmp == "%" :
                 trans = 7
             elif tmp == "/" :
                 trans = -1
             
             total += trans * 8**i

        print(total)
                 
            