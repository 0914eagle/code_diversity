def specialFilter(nums):
    
    return len([num for num in nums if num > 10 and num % 10 % 2 and num % 100 % 2])

print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))