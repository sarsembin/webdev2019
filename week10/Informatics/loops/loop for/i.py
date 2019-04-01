import math
a = int(input())
if a == 1:
    print(1)

else:
    counter = 0
    squareroot = int(math.sqrt(a))
    for x in range(1, squareroot):
        if a % x == 0:
            counter += 1

    counter = 2*counter

    if a % squareroot == 0:
        counter += 1

    print(counter)


