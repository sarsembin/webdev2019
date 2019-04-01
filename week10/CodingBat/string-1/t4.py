def make_out_word(out, word):
    middle = len(out) / 2
    x = ""
    for i in range(0, len(word) + len(out)):
        if i < middle:
            x += out[i]
        if i >= middle and i < middle + len(word):
            x += word[i - middle]
        if i >= middle + len(word):
            x += out[i - len(word)]
    return x


