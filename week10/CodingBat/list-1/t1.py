def first_last6(nums):
  if len(nums) == 1 and nums[0] == 6:
    return True
  elif len(nums) == 1 and nums[0] != 6:
    return False
  if nums[0] == 6 or nums[len(nums) - 1] == 6:
    return True
  return False