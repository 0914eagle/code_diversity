def digitSum(s):
    
    sum = 0
    for i in range(len(s)):
        if s[i].isupper():
            sum += ord(s[i])
    return sum


print(digitSum("aAaaaXa"))
