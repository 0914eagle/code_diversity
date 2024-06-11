def digitSum(s):
    
    return sum([ord(x) for x in s if x.isupper()])


if __name__ == '__main__':
    print(digitSum(""))
    print