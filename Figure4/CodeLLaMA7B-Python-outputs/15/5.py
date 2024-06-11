def string_sequence(n: int) -> str:
    
    # return ' '.join(str(i) for i in range(n+1))
    result = ''
    for i in range(n+1):
        result += str(i) + ' '
    return result[:-1]


if