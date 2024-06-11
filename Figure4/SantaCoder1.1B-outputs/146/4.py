def specialFilter(nums):
    
    odd_count = 0
    for num in nums:
        if num > 10 and num % 10 == 0 and num % 100 != 0:
            odd_count += 1
    return odd_count

