

def order_by_points(nums):
    
    # Sort the list based on the sum of digits
    sorted_list = sorted(nums, key=lambda x: sum(map(int, str(abs(x)))))

    # If there are several items with the same sum of digits,
    # order them based on their index in the original list
    result = []
    sum_dict = {}
    for i, num in enumerate(sorted_list):
        sum_of_digits = sum(map(int, str(abs(num))))
        if sum_of_digits not in sum_dict:
            sum_dict[sum_of_digits] = [i]
        else:
            sum_dict[sum_of_digits].append(i)

    for key in sum_dict:
        for index in sum_dict[key]:
            result.append(sorted_list[index])

    return result


