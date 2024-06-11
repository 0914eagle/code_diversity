def how_many_times(string: str, substring: str) -> int:
    
    return sum(substring in s for s in string.split(' '))


