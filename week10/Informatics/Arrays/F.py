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
for i in range(1, len(s2)-1):
    if int(s2[i+1]) < int(s2[i]) and int(s2[i-1]) < int(s2[i]):
        n1 = n1 + 1;
    
'''if boolean == True:
    print("YES")
if boolean == False:
    print("NO")'''
        #s = s + str(s2[i]) + ' '
print(n1)
