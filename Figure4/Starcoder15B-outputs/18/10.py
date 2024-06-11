def how_many_times(string: str, substring: str) -> int:
    
    if not string or not substring:
        return 0
    return 1 + how_many_times(string[1:], substring) if string.startswith(substring) else how_many_times(string[1:], substring)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/