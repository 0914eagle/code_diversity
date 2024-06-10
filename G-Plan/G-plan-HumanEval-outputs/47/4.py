
def count_overlapping_substrings(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

def how_many_times(string: str, substring: str) -> int:
    return count_overlapping_substrings(string, substring)

# Test cases
print(how_many_times('', 'a'))  # 0
print(how_many_times('aaa', 'a'))  # 3
print(how_many_times('aaaa', 'aa'))  # 3
