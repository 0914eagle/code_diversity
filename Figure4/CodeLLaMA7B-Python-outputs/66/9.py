def digitSum(s):
    
    # 1. Take a string as input
    # 2. Iterate over the string
    # 3. Check if the character is upper
    # 4. If so, add the ASCII code to the sum
    # 5. Return the sum
    # 6. If not, do nothing
    # 7. If the string is empty, return 0
    sum = 0
    for char in s:
        if char.isupper():
            sum += ord(char)
    return sum


