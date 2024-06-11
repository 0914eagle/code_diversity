def minSubArraySum(nums):
    
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return min(nums[0], nums[1])
    if len(nums) == 3:
        return min(nums[0], nums[1]) + min(nums[2], nums[1])
    if len(nums) == 4:
        return min(nums[0], nums[1]) + min(nums[2], nums[3]) + min(nums[1], nums[3])
    if len(nums) == 5:
        return min(nums[0], nums[1]) + min(nums[2], nums[3]) + min(nums[4], nums[3]) + min(nums[1], nums[3]) + min(nums[2], nums[4]) + min(nums[0], nums[4])
    if len(nums) == 6:
        return min(nums[0], nums[1]) + min(nums[2], nums[3]) + min(nums[4], nums[5]) + min(nums[1], nums[3]) + min(nums[2], nums[5]) + min(nums[0], nums[5]) + min(nums[1], nums[4]) + min(nums[0], nums[4]) + min(nums[1], nums[5]) + min(nums[0], nums[5]) + min(nums[2], nums[4]) + min(nums[0], nums[4]) + min(nums[1], nums[4]) + min(nums[0], nums[5]) + min(nums[1], nums[5]) + min(nums[2], nums[4]) + min(nums[0], nums[4]) + min(nums[1], nums[4]) + min(nums[0], nums[5]) + min(nums[1], nums[5]) + min(nums[2], nums[4]) + min(nums[0], nums[4]) + min(nums[1], nums[4]) + min(nums[0], nums[5]) + min(nums[1], nums[5]) + min(nums[2], nums[4]) + min(nums[0], nums[