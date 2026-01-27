import sys

while True:
    s = sys.stdin.readline()
    if s == "***":
        break
    print(s[::-1])
