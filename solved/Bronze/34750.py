import sys

n = int(sys.stdin.readline().rstrip())

mine = 0
parents = 0

if n >= 1000000 :
    mine = int(n * 0.2)
    parents = n - mine
elif n < 1000000 and n >= 500000 :
    mine = int(n * 0.15)
    parents = n - mine
elif n < 500000 and n >= 100000 :
    mine = int(n * 0.1)
    parents = n - mine
else :
    mine = int(n * 0.05)
    parents = n - mine

print(mine, end=" ")
print(parents)