
def how_many_times(string: str, substring: str) -> int:
    count = 0
    if not string or not substring:
        return 0
    
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    
    return count

# Test cases
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
