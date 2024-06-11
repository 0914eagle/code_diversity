def how_many_times(string: str, substring: str) -> int:
    
    if len(substring) > len(string):
        return 0
    elif len(substring) == len(string):
        return 1 if substring == string else 0
    else:
        return string.count(substring)


if