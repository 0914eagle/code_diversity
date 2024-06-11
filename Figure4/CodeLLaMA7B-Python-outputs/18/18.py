def how_many_times(string: str, substring: str) -> int:
    
    if len(substring) > len(string):
        return 0
    if len(substring) == 0:
        return len(string)
    if len(substring) == len(string):
        return 1 if string == substring else 0
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count


if __