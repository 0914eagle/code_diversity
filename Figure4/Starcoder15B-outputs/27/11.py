def flip_case(string: str) -> str:
    
    return ''.join(map(lambda c: c.lower() if c.isupper() else c.upper(), string))


