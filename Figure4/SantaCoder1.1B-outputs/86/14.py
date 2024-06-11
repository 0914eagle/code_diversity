def anti_shuffle(s):
    
    s = s.split()
    s.sort(key=lambda x: ord(x))
    return ' '.join(s)


