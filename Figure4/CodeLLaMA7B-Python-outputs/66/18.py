def digitSum(s):
    
    return sum(ord(c) for c in s if c.isupper())


if __name__ == '__main__':
    print(digitSum(""))
    print(