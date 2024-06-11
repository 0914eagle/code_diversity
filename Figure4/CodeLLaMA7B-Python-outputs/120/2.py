def maximum(arr, k):
    
    if not arr or k == 0:
        return []

    # find the max number in arr
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num

    # find the max k numbers in arr
    max_k_nums = []
    for num in arr:
        if num == max_num:
            max_k_nums.append(num)
            if len(max_k_nums) == k:
                break

    return sorted(max_k_nums)


