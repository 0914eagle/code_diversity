
def get_minimum_cards_to_verify(s):
    vowels = ["a", "e", "i", "o", "u"]
    even_digits = ["0", "2", "4", "6", "8"]
    count = 0
    for i in range(len(s) - 1):
        if s[i] in vowels and s[i + 1] not in even_digits:
            count += 1
        elif s[i] not in vowels and s[i + 1] in even_digits:
            count += 1
    return count

