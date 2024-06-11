def anti_shuffle(s):
    
    # Your code here
    return ' '.join(sorted(s.split(), key=lambda x: sorted(x)))


