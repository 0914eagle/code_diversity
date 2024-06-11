def hex_key(num):
    
    num = num.upper()
    count = 0
    for i in range(len(num)):
        if num[i] == 'A' or num[i] == 'B' or num[i] == 'C' or num[i] == 'D' or num[i] == 'E' or num[i] == 'F':
            count += 1
    return count

print(hex_key("AB"))
print(hex_key("1077E"))
print(hex_key("ABED1A33"))
print(hex_key("123456789ABCDEF0"))
print(hex_key("2020"))