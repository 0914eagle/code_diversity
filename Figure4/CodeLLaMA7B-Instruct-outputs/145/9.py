

def order_by_points(nums):
    
    # Sort the list based on the sum of the digits of each number
    sorted_nums = sorted(nums, key=lambda x: sum(map(int, str(x))))

    # If there are several items with the same sum of digits,
    # order them based on their index in the original list
    sorted_nums.sort(key=nums.index)

    return sorted_nums

# Test case 1:
assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
# Test case 2:
assert order_by_points([]) == []
# Test case 3:
assert
