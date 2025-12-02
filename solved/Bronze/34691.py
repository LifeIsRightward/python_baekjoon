import sys

while(True) :
    in_val = sys.stdin.readline().rstrip()

    if in_val == "end" :
        break
    elif in_val == "animal" :
        print("Panthera tigris")
    elif in_val == "tree" : 
        print("Pinus densiflora")
    elif in_val == "flower" :
        print("Forsythia koreana")