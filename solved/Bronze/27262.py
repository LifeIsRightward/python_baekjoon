import sys

n, k, a, b = map(int, sys.stdin.readline().rstrip().split())

misha = (n-1) * a
eve = (k-1) * 3 + (n-1) * 3

print(f'{eve} {misha}')