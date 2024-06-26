from math import gcd
def solve(nums):
   if len(nums) == 1:
      return nums[0]
   div = gcd(nums[0], nums[1])
   if len(nums) == 2:
      return div
   for i in range(1, len(nums) - 1):
      div = gcd(div, nums[i + 1])
      if div == 1:
         return div
   return div

nums = [300,900,600,1200]
print(solve(nums))