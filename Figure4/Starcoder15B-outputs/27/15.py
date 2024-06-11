def flip_case(string: str) -> str:
    
    return ''.join(map(lambda c: c.upper() if c.islower() else c.lower(), string))


