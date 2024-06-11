def specialFilter(nums):
    
    return len([x for x in nums if x > 10 and x % 10 % 2 == 1 and x % 100 % 2 == 1])

print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))