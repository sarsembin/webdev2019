def alarm_clock(day, vacation):
  w = "7:00" if not vacation else "10:00"
  wd = "10:00" if not vacation else "off"
  return w if day not in [6,0] else wd
