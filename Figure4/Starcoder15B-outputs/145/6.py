def order_by_points(nums):
    
    # Your code here
    # return sorted(nums, key=lambda x: sum(map(int, str(abs(x)))))
    return sorted(nums, key=lambda x: (sum(map(int, str(abs(x)))), x))


