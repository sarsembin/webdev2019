def front_back(str):
    if len(str) <= 1:
        return str

    xd = len(str) - 1
    x = str[1:xd]
    return str[xd] + x + str[0]