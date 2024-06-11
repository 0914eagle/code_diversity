def minSubArraySum(nums):
    
    # Write your code here
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(nums[0], nums[1])
    if len(nums) == 3:
        return min(nums[0], min(nums[1], nums[2]))
    if len(nums) == 4:
        return min(nums[0], min(nums[1], nums[2]), min(nums[3], nums[4]))
    if len(nums) == 5:
        return min(nums[0], min(nums[1], nums[2]), min(nums[3], nums[4]), min(nums[5], nums[6]))
    if len(nums) == 6:
        return min(nums[0], min(nums[1], nums[2]), min(nums[3], nums[4]), min(nums[5], nums[6]), min(nums[7], nums[8]))
    if len(nums) == 7:
        return min(nums[0], min(nums[1], nums[2]), min(nums[3], nums[4]), min(nums[5], nums[6]), min(nums[7], nums[8]), min(nums[9], nums[10]))
    if len(nums) == 8:
        return min(nums[0], min(nums[1], nums[2]), min(nums[3], nums[4]), min(nums[5], nums[6]), min(nums[7], nums[8]), min(nums[9], nums[10]), min(nums[11], nums[12]))
    if len(nums) == 9:
        return min(nums[0], min(nums[1], nums[2]), min(nums[3], nums[4]), min(nums[5], nums[6]), min(nums[7], nums[8]), min(nums[9], nums[10]), min(nums[11], nums[12]), min(nums[13], nums[14]))
    if len(nums) == 10:
        return min(nums[0], min(nums[1], nums[2]), min(nums[3], nums[4]), min(nums[5