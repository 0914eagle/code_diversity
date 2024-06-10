
def how_many_times(string: str, substring: str) -> int:
    if not string or not substring:
        return 0

    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1

    return count

print(how_many_times('', 'a'))
print(how_many_times('aaa', 'a'))
print(how_many_times('aaaa', 'aa'))
