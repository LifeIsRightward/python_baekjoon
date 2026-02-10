import sys

x_cost = int(sys.stdin.readline().rstrip())
y_basic_cost = int(sys.stdin.readline().rstrip())
y_basic_standard = int(sys.stdin.readline().rstrip())
y_additional_cost = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())

x_total = x_cost * p
y_total = 0

if(p > y_basic_standard) :
     y_total = (p - y_basic_standard) * y_additional_cost + y_basic_cost
else :
     y_total = y_basic_cost

if (x_total > y_total) :
     print(y_total)
else :
     print(x_total)