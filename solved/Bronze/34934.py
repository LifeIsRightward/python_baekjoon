import sys

n = int(sys.stdin.readline().rstrip())

sub = " "
year = 0

for i in range(n) :
    insub, inyear = sys.stdin.readline().rstrip().split()
    inyear = int(inyear)

    if year < inyear :
        year = inyear
        sub = insub

print(sub)