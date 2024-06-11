def anti_shuffle(s):
    
    # Your code here
    s = s.split()
    s.sort(key=lambda x: ord(x))
    s = ' '.join(s)
    return s


