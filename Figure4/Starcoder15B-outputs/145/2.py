def order_by_points(nums):
    
    # your code here
    return sorted(nums, key=lambda x: sum(map(int, str(abs(x)))))


