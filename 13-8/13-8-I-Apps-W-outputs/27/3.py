
def min_cards_to_verify_statement(s):
    vowels = set("aeiou")
    even_digits = set("02468")
    vowel_cards = 0
    even_digit_cards = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].lower() in vowels:
                vowel_cards += 1
            if s[i].isdigit() and int(s[i]) in even_digits:
                even_digit_cards += 1
        else:
            if s[i-1].isalpha() and s[i-1].lower() in vowels:
                vowel_cards += 1
            if s[i-1].isdigit() and int(s[i-1]) in even_digits:
                even_digit_cards += 1
    return max(vowel_cards, even_digit_cards)

