def specialFilter(nums):
    
    count = 0
    for i in range(len(nums)):
        if nums[i] > 10 and nums[i] % 2 == 1:
            count += 1
    return count

