if __name__ == '__main__':
    n = int(input())
    integer_list=input().strip().split()
    l = []
    for i in range(0, n):
        l.append(int(integer_list[i]))

    t = tuple(l)

    print (hash(t))

