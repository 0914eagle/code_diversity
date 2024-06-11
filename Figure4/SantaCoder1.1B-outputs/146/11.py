def specialFilter(nums):
    
    return sum(1 for x in nums if x > 10 and (x % 10) % 2 == 1)

