
def string_xor(a: str, b: str) -> str:
    
    if len(a) != len(b):
        raise ValueError("Input strings must have the same length.")
    
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    
    return result
