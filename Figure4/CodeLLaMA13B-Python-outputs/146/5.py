def specialFilter(nums):
    
    return len([n for n in nums if n > 10 and n % 10 % 2 and n % 100 % 2])

print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))