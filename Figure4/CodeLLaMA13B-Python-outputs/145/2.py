def order_by_points(nums):
    
    return sorted(nums, key=lambda x: (sum(int(y) for y in str(x)), x))


if