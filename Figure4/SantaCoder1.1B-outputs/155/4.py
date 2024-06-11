def even_odd_count(num):
    
    count = 0
    for i in str(num):
        if i.isdigit():
            count += 1
    return count, count


