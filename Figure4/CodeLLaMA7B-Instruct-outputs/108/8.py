

def count_nums(arr):
    
    count = 0
    for num in arr:
        if num < 0:
            count += 1
        else:
            count += len(str(num))
    return count


