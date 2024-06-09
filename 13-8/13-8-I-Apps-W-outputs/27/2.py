
def min_cards_to_verify_statement(s):
    vowels = set("aeiou")
    even_digits = set("02468")
    vowel_cards, even_digit_cards = 0, 0
    for i in range(len(s) // 2):
        if s[2*i] in vowels:
            vowel_cards += 1
        if s[2*i+1] in even_digits:
            even_digit_cards += 1
    return max(vowel_cards, even_digit_cards)

