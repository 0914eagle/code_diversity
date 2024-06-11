def even_odd_count(num):
    
    even_count = 0
    odd_count = 0
    for digit in str(num):
        if digit == '0':
            continue
        if digit == '1':
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


