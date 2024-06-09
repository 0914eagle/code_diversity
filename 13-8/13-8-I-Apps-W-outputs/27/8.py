
def solve(s):
    vowels = set("aeiou")
    even_digits = set("02468")
    vowel_count = 0
    even_digit_count = 0
    for i in range(len(s) - 1, -1, -2):
        if s[i] in vowels:
            vowel_count += 1
        if s[i - 1] in even_digits:
            even_digit_count += 1
    return max(vowel_count, even_digit_count)

