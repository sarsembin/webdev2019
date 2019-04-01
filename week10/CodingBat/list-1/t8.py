def max_end3(nums):
  max = 0
  maxarr = []

  if nums[0] > nums[len(nums) - 1]:
    max = nums[0]
  elif nums[0] < nums[len(nums) - 1]:
    max = nums[len(nums)- 1]
  elif nums[0] == nums[len(nums) - 1]:
    max = nums[len(nums)- 1]
  for i in range(0, len(nums)):
    maxarr.append(max)
  return maxarr