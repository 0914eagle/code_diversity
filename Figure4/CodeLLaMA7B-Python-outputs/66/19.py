def digitSum(s):
    
    # return sum([ord(i) for i in s if i.isupper()])
    return sum(ord(i) for i in s if i.isupper())


if