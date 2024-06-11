def encrypt(s):
    
    s = s.lower()
    result = ''
    for i in s:
        if i.isalpha():
            result += chr((ord(i) - 97 + 2) % 26 + 97)
        else:
            result += i
    return result


