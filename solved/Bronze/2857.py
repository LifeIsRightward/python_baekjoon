import sys

# answer list
li = []

for i in range(5):
    n = sys.stdin.readline().rstrip()    

    if 'FBI' in n :
        li.append(i+1)


if len(li) == 0 :
    print("HE GOT AWAY!")
else :
    for x in li:
        print(int(x), end=' ')
