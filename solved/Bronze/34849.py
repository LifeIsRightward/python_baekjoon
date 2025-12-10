import sys

n = int(sys.stdin.readline().rstrip())

if n**2 <= 10**8 :
    print("Accepted")
else :
    print("Time limit exceeded")