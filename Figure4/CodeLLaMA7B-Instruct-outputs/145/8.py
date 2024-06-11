

def order_by_points(nums):
    
    # Sort the list based on the sum of digits
    sorted_list = sorted(nums, key=lambda x: sum(map(int, str(abs(x)))))

    # If there are several items with the same sum of digits,
    # order them based on their index in the original list
    result = []
    sum_to_index = {}
    for i, num in enumerate(sorted_list):
        sum_to_index.setdefault(sum(map(int, str(abs(num)))) , []).append(i)

    for key, value in sum_to_index.items():
        for index in value:
            result.append(sorted_list[index])

    return result


