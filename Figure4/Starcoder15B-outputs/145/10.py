def order_by_points(nums):
    
    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))


