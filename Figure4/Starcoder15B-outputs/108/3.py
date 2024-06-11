def count_nums(arr):
    
    count = 0
    for i in arr:
        if sum(int(x) for x in str(i)) > 0:
            count += 1
    return count


