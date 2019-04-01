def front3(str):
    if len(str) < 3:
        return str + str + str
    else:
        x = str[0:3]
        return x + x + x
