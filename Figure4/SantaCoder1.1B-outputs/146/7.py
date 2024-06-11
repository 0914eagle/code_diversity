def specialFilter(nums):
    
    return sum([1 for num in nums if num > 10 and (num % 10) % 2 == 1])

