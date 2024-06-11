def how_many_times(string: str, substring: str) -> int:
    
    if len(substring) == 0:
        return 0
    return 1 + how_many_times(string[1:], substring) if string.startswith(substring) else how_many_times(string[1:], substring)


if