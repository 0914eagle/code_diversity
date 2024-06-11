def solve(s):
    
    # your code
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                s[i] = s[i].lower()
            else:
                s[i] = s[i].upper()
    if s.count('a') == 0 and s.count('A') == 0:
        s.reverse()
    else:
        s = ''.join(s)
    return s


if