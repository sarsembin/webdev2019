def make_ends(nums):
  arr = [1, 2]
  if len(nums) == 1:
    arr[0] = nums[0]
    arr[1] = nums[0]
    return arr
  else:
    arr[0]=nums[0]
    arr[1]=nums[len(nums) - 1]
    return arr
