

def order_by_points(nums):
    
    # Sort the list based on the sum of digits
    sorted_nums = sorted(nums, key=lambda x: sum(map(int, str(abs(x)))))

    # If there are several items with the same sum of digits,
    # order them based on their index in the original list
    sorted_nums.sort(key=nums.index)

    return sorted_nums

# Test
