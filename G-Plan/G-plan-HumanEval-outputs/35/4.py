
def vowels_count(s: str) -> int:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    for i in range(len(s)):
        if s[i].lower() in vowels:
            count += 1
        elif i == len(s) - 1 and s[i].lower() == 'y':
            count += 1
    return count

word = input().strip()
print(vowels_count(word))
