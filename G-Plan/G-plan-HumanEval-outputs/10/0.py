
def count_upper(s: str) -> int:
    vowels = set('AEIOU')
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count

# Test the function with example inputs
print(count_upper('aBCdEf'))
print(count_upper('abcdefg'))
print(count_upper('dBBE'))
