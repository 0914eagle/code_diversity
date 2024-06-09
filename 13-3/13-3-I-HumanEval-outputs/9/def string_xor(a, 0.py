
def string_xor(a: str, b: str) -> str:
    
    return ''.join('1' if x == '0' and y == '1' or x == '1' and y == '0' else '0' for x, y in zip(a, b))

