a = list()
n = int(input())
s1 = input()
n1 = 0
s2 = s1.split(' ')
'''for i in range(n):
    m = input()
    a.append(int(m))'''
s = ""
for i in range(1, len(s2)):
    if int(s2[i]) > int(s2[i-1]):
        n1 = n1 + 1
        #s = s + str(s2[i]) + ' '
print(n1)
