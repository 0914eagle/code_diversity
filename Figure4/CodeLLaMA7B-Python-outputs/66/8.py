def digitSum(s):
    
    # 1. Take a string as input
    # 2. Iterate over the string
    # 3. Check if the character is upper
    # 4. If so, add the character's ASCII code to the sum
    # 5. Return the sum

    # 1. Take a string as input
    s = s

    # 2. Iterate over the string
    sum = 0
    for i in s:
        # 3. Check if the character is upper
        if i.isupper():
            # 4. If so, add the character's ASCII code to the sum
            sum += ord(i)

    # 5. Return the sum
    return sum


#