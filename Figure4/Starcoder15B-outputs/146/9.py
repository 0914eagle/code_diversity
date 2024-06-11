def specialFilter(nums):
    
    return len([num for num in nums if num > 10 and num % 2 == 1 and num % 10 == 1])

