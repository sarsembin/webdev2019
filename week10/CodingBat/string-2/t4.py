def count_code(str):
  x = 0
  for i in range(0, len(str)):
    if str[i] == 'c'and i+1 < len(str):
      if str[i+1] == 'o' and i+2 < len(str):
        if i+3 < len(str):
          if str[i+3] == 'e':
            x += 1
  return x