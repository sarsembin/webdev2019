def caught_speeding(speed, is_birthday):
  spd = speed - (65 if is_birthday else 60)
  if spd > 20:
    return 2
  elif spd > 0:
    return 1
  else:
    return 0
