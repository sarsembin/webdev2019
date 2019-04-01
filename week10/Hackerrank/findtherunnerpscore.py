if __name__ == '__main__':
    n = int(input())
elements = input().strip().split()
l = []
for i in elements:
    l.append(int(i))

l.sort(reverse=True)
largest = l[0]

for i in l:
    if i != largest:
        print (i)
        break

