def specialFilter(nums):
    
    return sum(1 for n in nums if n > 10 and (n % 10) % 2 == 1)

