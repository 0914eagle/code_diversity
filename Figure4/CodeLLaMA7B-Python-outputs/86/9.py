def anti_shuffle(s):
    
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s
    if len(s) == 2:
        return s[0] + s[1]

    if ' ' in s:
        return ' '.join(sorted(s.split(), key=lambda x: ''.join(sorted(x))))
    else:
        return ''.join(sorted(s))


if