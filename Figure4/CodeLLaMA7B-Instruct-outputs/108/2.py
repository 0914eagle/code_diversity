

def count_nums(arr):
    
    count = 0
    for num in arr:
        if sum(map(lambda x: x >= 0, str(num))) > 0:
            count += 1
    return count


