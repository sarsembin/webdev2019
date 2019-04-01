def string_bits(str):
    x = ""
    for i in range(0, len(str)):
        if i % 2 == 0:
            x += str[i]
    return x

