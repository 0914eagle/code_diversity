def order_by_points(nums):
    
    return sorted(nums, key=lambda x: (sum(int(i) for i in str(x)), nums.index(x)))


if