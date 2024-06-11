def hex_key(num):
    
    # Your code here
    num = num.upper()
    count = 0
    for i in num:
        if i in "ABCDEF0":
            count += 1
    return count

