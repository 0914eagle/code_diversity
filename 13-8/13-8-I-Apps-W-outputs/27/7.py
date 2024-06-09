
def min_cards_to_verify(s):
    vowels = set("aeiou")
    even_digits = set("02468")
    vowel_cards = 0
    even_digit_cards = 0
    for char in s:
        if char in vowels:
            vowel_cards += 1
        elif char in even_digits:
            even_digit_cards += 1
    return max(vowel_cards, even_digit_cards)

