def digitSum(s):
    
    sum = 0
    for char in s:
        if char.isupper():
            sum += ord(char)
    return sum


print(digitSum(""))
print(digitSum("abAB"))
print(digitSum("abcCd"))
print(digitSum("helloE"))
print(digitSum("woArBld"))
print(digitSum("aAaaaXa"))
