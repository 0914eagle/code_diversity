def how_many_times(string: str, substring: str) -> int:
    
    if not string or not substring:
        return 0
    if len(substring) > len(string):
        return 0
    if substring == string:
        return 1
    return how_many_times(string[1:], substring) + how_many_times(string[1:], substring[1:])


if __name__ == '__main