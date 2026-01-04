import sys

n = int(sys.stdin.readline().rstrip())

l1 = list(map(int, sys.stdin.readline().rstrip().split()))
l2 = list(map(int, sys.stdin.readline().rstrip().split()))
l3 = list(map(int, sys.stdin.readline().rstrip().split()))

# lb1 = False
# lb2 = False
# lb3 = False

if 7 in l1 and 7 in l2 and 7 in l3 :
    print("777")
else :
    print("0")

# for x in l1 :
#     if x == 7 :
#         lb1 = True

# for x in l2 :
#     if x == 7 :
#         lb2 = True

# for x in l3 :
#     if x == 7 :
#         lb3 = True

# if lb1 and lb2 and lb3 == True :
#     print("777")
# else :
#     print("0")