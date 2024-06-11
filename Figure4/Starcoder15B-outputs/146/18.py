def specialFilter(nums):
    
    count = 0
    for num in nums:
        if num > 10 and num % 2 == 1 and num % 10 % 2 == 1:
            count += 1
    return count


