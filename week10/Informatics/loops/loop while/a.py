import math
a = int(input())
b=1
while b <= a:
    j = math.sqrt(b)
    j = int(j)
    if j*j == b:
        print(b)
    b =b+1