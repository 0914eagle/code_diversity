def digitSum(s):
    
    return sum([ord(i) for i in s if i.isupper()])


if __name__ == '__main__':
    print(digitSum(""))
    print(digitSum("abAB"))
    print(digitSum("abcCd"))
    print(digitSum("helloE"))
    print(digitSum("woArBld"))
    print(digit