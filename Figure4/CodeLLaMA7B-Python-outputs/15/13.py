def string_sequence(n: int) -> str:
    
    # return ' '.join(str(i) for i in range(n+1))
    s = ''
    for i in range(n+1):
        s += str(i) + ' '
    return s[:-1]


