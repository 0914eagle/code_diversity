def digitSum(s):
    
    return sum([ord(x) for x in s if x.isupper()])


print(digitSum(""))
print(digitSum("abAB"))
print(digitSum("abcCd"))
print(digitSum("helloE"))
print(digitSum("woArBld"))
print(digitSum("aAaaaXa"))
