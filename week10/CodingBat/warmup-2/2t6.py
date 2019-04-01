def array_count9(nums):
  x = 0
  for i in range(0, len(nums)):
    if nums[i] == 9:
      x += 1
  return x
