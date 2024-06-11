def how_many_times(string: str, substring: str) -> int:
    
    if not string or not substring:
        return 0
    if substring not in string:
        return 0
    return 1 + how_many_times(string[string.index(substring) + 1:], substring)


