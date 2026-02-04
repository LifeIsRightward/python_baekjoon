import sys

n, m = list(map(int, sys.stdin.readline().rstrip().split()))

ddukbbagie = list(map(int, sys.stdin.readline().rstrip().split()))
zzoggi = list(map(int, sys.stdin.readline().rstrip().split()))

ddukmax = max(ddukbbagie)
zzoggimax = max(zzoggi)

print(ddukmax + zzoggimax)