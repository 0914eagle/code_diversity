
def string_xor(a: str, b: str) -> str:
    
    if len(a) != len(b):
        raise ValueError("Input strings must be of equal length.")
    
    result = ""
    for char1, char2 in zip(a, b):
        if char1 == char2:
            result += '0'
        else:
            result += '1'
    
    return result
