def count_hi(str):
  x = 0
  for i in range(0, len(str)):
    if str[i] == 'h'and i+1 < len(str):
      if str[i+1] == 'i':
        x += 1
  return x
