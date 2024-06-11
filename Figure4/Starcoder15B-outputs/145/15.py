def order_by_points(nums):
    
    # your code here
    if not nums:
        return []
    else:
        return sorted(nums, key=lambda x: (sum(map(int, str(abs(x)))), nums.index(x)))


