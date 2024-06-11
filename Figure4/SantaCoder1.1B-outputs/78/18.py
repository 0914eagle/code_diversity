def hex_key(num):
    
    num = num.upper()
    num_len = len(num)
    if num_len == 0:
        return 0
    if num_len == 1:
        return 1
    if num_len == 2:
        if num[0] == '0' and num[1] == '0':
            return 0
        if num[0] == '0' and num[1] == '1':
            return 1
        if num[0] == '1' and num[1] == '0':
            return 1
        if num[0] == '1' and num[1] == '1':
            return 2
    if num_len == 3:
        if num[0] == '0' and num[1] == '0' and num[2] == '0':
            return 0
        if num[0] == '0' and num[1] == '0' and num[2] == '1':
            return 1
        if num[0] == '0' and num[1] == '1' and num[2] == '0':
            return 1
        if num[0] == '0' and num[1] == '1' and num[2] == '1':
            return 2
        if num[0] == '1' and num[1] == '0' and num[2] == '0':
            return 1
        if num[0] == '1' and num[1] == '0' and num[2] == '1':
            return 1
        if num[0] == '1' and num[1] == '1' and num[2] == '0':
            return 1
        if num[0] == '1' and num[1] == '1' and num[2] == '1':
            return 2
    if num_len == 4:
        if num[0] == '0' and num[1] == '0' and num[2] == '0' and num[3] == '0':
            return 0
        if num[0] == '0' and num[1] == '0' and num[2] == '0' and num[3] == '1':
            return 1
        if num[0] == '0' and num[