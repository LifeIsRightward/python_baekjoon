arr = list(map(int, input().split()))
total = 0

# arr 처음부터 끝까지 -> 정확히 말하면, arr 리스트의 원소가 없을때 까지를 이야기하는거임.
# arr 리스트에 하나하나씩 접근하는거는 i 인거고
for i in arr :
    total += i

print(total)