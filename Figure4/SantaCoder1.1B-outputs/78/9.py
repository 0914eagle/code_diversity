def hex_key(num):
    
    # Your code here
    num = num.upper()
    count = 0
    for i in range(len(num)):
        if num[i] == 'A' or num[i] == 'B' or num[i] == 'C' or num[i] == 'D' or num[i] == 'E' or num[i] == 'F':
            count += 1
    return count

