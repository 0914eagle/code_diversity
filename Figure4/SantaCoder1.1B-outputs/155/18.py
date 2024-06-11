def even_odd_count(num):
    
    even_count = 0
    odd_count = 0
    for i in range(len(str(num))):
        if str(num)[i] == '0':
            continue
        elif str(num)[i] == '1':
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)


