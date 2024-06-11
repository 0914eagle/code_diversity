

def order_by_points(nums):
    
    # Sort the list based on the sum of digits
    sorted_list = sorted(nums, key=lambda x: sum(map(int, str(x))))

    # If there are several items with the same sum of digits,
    # order them based on their index in the original list
    result = []
    for i in range(len(sorted_list)):
        if i == 0 or sum(map(int, str(sorted_list[i]))) != sum(map(int, str(sorted_list[i-1]))):
            result.append(sorted_list[i])

    return result


