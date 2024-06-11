def how_many_times(string: str, substring: str) -> int:
    
    if substring == '':
        return 0
    if string == '':
        return 0
    if string.startswith(substring):
        return 1 + how_many_times(string[len(substring):], substring)
    else:
        return how_many_times(string[1:], substring)


