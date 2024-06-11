def specialFilter(nums):
    
    return len([x for x in nums if (x > 10 and (x % 10) % 2 != 0 and (x // 10) % 2 != 0)])

