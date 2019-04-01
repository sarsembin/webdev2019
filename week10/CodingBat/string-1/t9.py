def combo_string(a, b):
  if len(b) > len(a):
    return a + b + a
  elif len(a) > len(b):
    return b + a + b
