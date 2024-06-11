def anti_shuffle(s):
    
    s = s.split()
    for i in range(len(s)):
        s[i] = ''.join(sorted(s[i]))
    return ' '.join(s)


