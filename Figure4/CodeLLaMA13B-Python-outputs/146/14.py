def specialFilter(nums):
    
    count = 0
    for num in nums:
        if num > 10 and num % 10 % 2 != 0 and num % 100 % 2 != 0:
            count += 1
    return count

print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))