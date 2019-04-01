def string_splosion(str):
  x = ""
  for i in range(0,len(str) + 1):
    x += str[0:i]
  return x
