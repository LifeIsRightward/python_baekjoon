import sys

arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

if arr1[0] + arr2[0] == arr1[1] + arr2[1] :
    print("Either")
elif arr1[0] + arr2[0] > arr1[1] + arr2[1] : 
    print("Yongdap")
elif arr1[0] + arr2[0] < arr1[1] + arr2[1] :
    print("Hanyang Univ.")