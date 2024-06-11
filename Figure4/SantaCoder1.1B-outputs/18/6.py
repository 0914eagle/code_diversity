def how_many_times(string: str, substring: str) -> int:
    
    return sum(1 for s in string.split(substring) if substring in s)


