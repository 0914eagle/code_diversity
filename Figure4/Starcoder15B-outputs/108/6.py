def count_nums(arr):
    
    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1
    return count

