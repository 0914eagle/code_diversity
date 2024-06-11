def order_by_points(nums):
    
    if not nums:
        return []
    return sorted(nums, key=lambda x: (sum(map(int, str(abs(x)))), nums.index(x)))


