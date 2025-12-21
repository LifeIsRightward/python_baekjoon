import sys

while True :
    x, y = map(int, sys.stdin.readline().rstrip().split)

    if x + y == 0 :
        break 
    else :
        if x + y == 13:
            print("Never speak again.")
        else :
            if x > y :
                print("To the convention.")
            elif x < y :
                print("Left beehind.")
            elif x == y :
                print("Undecided.")