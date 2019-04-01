step = 1
kolvo = 0
a = int(input())

while a > step:
    step = step<<1
    kolvo = kolvo + 1

print(kolvo)