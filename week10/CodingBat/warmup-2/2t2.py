def front_times(str, n):
  x = ""
  if len(str) <= 3:
    for i in range(0, n):
      x += str
    return x
  else:
    for i in range(0, n):
      x += str[0:3]
    return x


