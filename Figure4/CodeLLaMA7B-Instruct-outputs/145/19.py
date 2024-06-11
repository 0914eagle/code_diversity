

def order_by_points(nums):
    
    # Sort the list based on the sum of digits
    sorted_list = sorted(nums, key=lambda x: sum(map(int, str(x))))

    # If there are several items with the same sum of digits,
    # order them based on their index in the original list
    result = []
    sum_to_index = {}
    for i, num in enumerate(sorted_list):
        sum_to_index.setdefault(sum(map(int, str(num))), []).append(i)
    for sum_of_digits, indices in sum_to_index.items():
        for index in indices:
            result.append(sorted_list[index])

    return result


