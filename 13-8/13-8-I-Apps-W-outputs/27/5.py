
def get_minimum_cards_to_verify(sides):
    vowels = set("aeiou")
    even_digits = set("02468")
    vowel_digits = set()
    for i in range(0, len(sides), 2):
        if sides[i] in vowels:
            vowel_digits.add(sides[i+1])
    return len(vowel_digits) - len(even_digits.intersection(vowel_digits))

