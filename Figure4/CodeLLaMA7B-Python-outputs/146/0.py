def specialFilter(nums):
    
    # return len([num for num in nums if num > 10 and num % 10 in [1, 3, 5, 7, 9] and num // 10 % 2 == 1])
    return len([num for num in nums if num > 10 and num % 10 in [1, 3, 5, 7, 9] and num // 10 % 2 == 1])


print(specialFilter([15, -73, 14, -15]))
print(specialFilter([33, -2, -3, 45, 21, 109]))
