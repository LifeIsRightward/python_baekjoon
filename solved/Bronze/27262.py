import sys

n, k, a, b = map(int, sys.stdin.readline().rstrip().split())

misha = (n-1) * a
eve = (k-1) * b + (n-1) * b

print(f'{eve} {misha}')