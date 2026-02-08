import sys

n = sys.stdin.readline().rstrip()

le = len(n) // 2

print(f"{n[0:le]} {n[le:]}")