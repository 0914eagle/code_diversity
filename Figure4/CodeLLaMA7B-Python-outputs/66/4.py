def digitSum(s):
    
    # 1. Take a string as input
    # 2. Convert the string to a list
    # 3. Iterate through the list and sum the upper characters
    # 4. Return the sum

    # 1. Take a string as input
    s = s

    # 2. Convert the string to a list
    s_list = list(s)

    # 3. Iterate through the list and sum the upper characters
    sum = 0
    for i in s_list:
        if i.isupper():
            sum += ord(i)

    # 4. Return the sum
    return sum


#