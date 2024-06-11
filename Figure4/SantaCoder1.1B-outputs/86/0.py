def anti_shuffle(s):
    
    s = s.lower()
    s = s.split()
    s = sorted(s, key=lambda x: (ord(x[0]), x[1:]))
    return ' '.join(s)


