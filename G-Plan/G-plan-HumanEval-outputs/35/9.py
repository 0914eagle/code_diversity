
def vowels_count(s: str) -> int:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    for i, char in enumerate(s):
        if char.lower() in vowels or (char.lower() == 'y' and i == len(s) - 1):
            count += 1
    return count

# Test the function with example inputs
print(vowels_count('abcde'))
print(vowels_count('ACEDY'))
