def specialFilter(nums):
    
    count = 0
    for i in nums:
        if i > 10 and (i % 10) % 2 == 1:
            count += 1
    return count

