def hex_key(num):
    
    num = num.upper()
    num_list = list(num)
    num_list.sort()
    num_list.reverse()
    count = 0
    for i in range(len(num_list)):
        if num_list[i] == '0':
            continue
        if num_list[i] == '1':
            count += 1
    return count


