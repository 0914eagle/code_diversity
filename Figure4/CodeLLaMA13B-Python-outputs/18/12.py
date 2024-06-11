def how_many_times(string: str, substring: str) -> int:
    
    if len(substring) == 0:
        return 0
    return string.count(substring, 0, len(string))


if __name__ == '__main__