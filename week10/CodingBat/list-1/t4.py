def common_end(a, b):
  if len(a) == 1 and len(b) != 1:
    if a[0] == b[0] or a[0] == b[len(b)-1]:
      return True
  if len(a) != 1 and len(b) == 1:
   if a[0] == b[0] or a[len(a)-1] == b[0]:
     return True
  if len(a) == 1 and len(b) == 1:
   if a[0] == b[0]:
     return True
  if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
    return True
  return False
