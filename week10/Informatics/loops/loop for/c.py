import math
a = int(input())
b = int(input())

for x in range(a, b+1):
    square = int(math.sqrt(float(x)))
    if square == 0:
        continue
    if square*square == x:
        print(x)

#secind solution
# while a<=b:
#     j = math.sqrt(a)
#     j = (int)j
#     if j*j == a:
#         print(a)
#     a +=1