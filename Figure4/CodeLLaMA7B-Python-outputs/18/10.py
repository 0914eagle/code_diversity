def how_many_times(string: str, substring: str) -> int:
    
    if len(string) == 0 or len(substring) == 0:
        return 0
    if len(string) < len(substring):
        return 0
    if len(string) == len(substring):
        return 1 if string == substring else 0

    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count


if