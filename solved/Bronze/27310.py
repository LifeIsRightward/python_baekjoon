import sys

emo = sys.stdin.readline().rstrip()

l = len(emo)
col = 0
under = 0

for x in emo :
    if x == ':' :
        col += 1
    elif x == '_' :
        under += 1

print (l + col + under * 5)