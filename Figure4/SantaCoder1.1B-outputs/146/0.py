def specialFilter(nums):
    
    return sum([1 if i%2==0 and i>10 else 0 for i in nums])

