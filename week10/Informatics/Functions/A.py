def min4(a, b, c, d):
    return min(min(a, b), min(c, d))
def power(a, n):
    k = 1
    for i in range (0, n):
        k = k * a
    return k
si = input()
s = si.split(' ')
print(min4(s[0], s[1], s[2], s[3])
