
def vowels_count(s: str) -> int:
    vowels = set('aeiou')
    count = 0
    for i in range(len(s)):
        if s[i].lower() in vowels:
            if i == len(s) - 1 or (i == len(s) - 2 and s[i].lower() == 'y'):
                count += 1
    return count

# Test the function with example inputs
print(vowels_count('abcde'))
print(vowels_count('ACEDY'))
