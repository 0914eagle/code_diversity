
def is_bored(S: str) -> int:
    
    return len([s for s in S.split('.') if s.strip().startswith('I')])

