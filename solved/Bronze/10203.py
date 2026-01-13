import sys

n = int(sys.stdin.readline().rstrip())

vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(n) :
    tmp = sys.stdin.readline().rstrip()
    cnt = 0

    for y in tmp :
        if y in vowels :
            cnt += 1
    
    print(f'The number of vowels in {tmp} is {cnt}.')