def solve(s):
    
    result = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                result += i.upper()
            else:
                result += i.lower()
        else:
            result += i
    return result if result else s[::-1]


if __name__ == '__main__':
    print(solve("1234"))
    print(solve("ab"))
    print(solve("#a@C"))
