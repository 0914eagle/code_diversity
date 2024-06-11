def anti_shuffle(s):
    
    return ' '.join(sorted(word, key=lambda x: ord(x)) for word in s.split())


