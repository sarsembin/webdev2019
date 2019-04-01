def array123(nums):
  for i in nums:
     if i+2<len(nums):
      if (nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
        return True
     if len(nums) == 3:
       if (nums[0] == 1 and nums[1] == 2 and nums[2] == 3):
        return True
  return False
