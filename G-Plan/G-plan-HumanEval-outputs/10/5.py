
def is_uppercase_vowel(char: str) -> bool:
    return char in ['A', 'E', 'I', 'O', 'U']

def count_upper(s: str) -> int:
    count = 0
    for i in range(0, len(s), 2):
        if is_uppercase_vowel(s[i]) and s[i].isupper():
            count += 1
    return count

s = input().strip()
print(count_upper(s))
