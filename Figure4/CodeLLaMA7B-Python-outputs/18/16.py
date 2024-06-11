def how_many_times(string: str, substring: str) -> int:
    
    return string.count(substring)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
