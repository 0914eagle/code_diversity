def how_many_times(string: str, substring: str) -> int:
    
    if len(substring) > len(string):
        return 0
    if len(substring) == 0:
        return len(string)
    if len(string) == 0:
        return 0
    if string[0] == substring[0]:
        return 1 + how_many_times(string[1:], substring[1:])
    return how_many_times(string[1:], substring)


if