a = list()
n = int(input())
s1 = input()
n1 = 0
boolean = False
s2 = s1.split(' ')
'''for i in range(n):
    m = input()
    a.append(int(m))'''
s = ""

for i in list(reversed(s2)):
    s = s + str(i) + ' '
    
'''if boolean == True:
    print("YES")
if boolean == False:
    print("NO")'''

print(s)
