def min4(a, b, c, d):
    return min(min(a, b), min(c, d))
def power(a, n):
    k = 1
    for i in range (0, n):
        k = k * a
    return k
def xor(a, b):
    if (a == 1 and b == 1):
        return 0
    elif ( (a==1 and b==0) or (a==0 and b==1) ):
        return 1
    else:
        return 0
si = input()
s = si.split(' ')
print(xor(int(s[0]), int(s[1]) ) )
