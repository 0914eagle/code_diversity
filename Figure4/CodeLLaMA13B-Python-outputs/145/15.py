def order_by_points(nums):
    
    return sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))


if