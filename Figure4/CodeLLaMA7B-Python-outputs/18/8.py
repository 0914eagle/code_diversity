def how_many_times(string: str, substring: str) -> int:
    
    if len(substring) == 0:
        return 0
    if len(string) == 0:
        return 0
    if len(string) < len(substring):
        return 0
    if len(string) == len(substring):
        return 1 if string == substring else 0
    if len(string) > len(substring):
        return string.count(substring)


if