
def vowels_count(s: str) -> int:
    vowels = set('aeiou')
    count = 0
    for i in range(len(s)):
        if s[i].lower() in vowels:
            count += 1
        elif i == len(s) - 1 and s[i].lower() == 'y':
            count += 1
    return count

# Input reading
word = input().strip()

# Output
print(vowels_count(word))
