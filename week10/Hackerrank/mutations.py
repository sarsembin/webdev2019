def mutate_string(str1, ind, ch):
    l1 = list(str1)
    l1[ind] = ch
    str1 = ''.join(l1)
    return str1

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)