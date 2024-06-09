
def get_minimum_cards_to_verify(sides):
    vowels = ["a", "e", "i", "o", "u"]
    evens = ["0", "2", "4", "6", "8"]
    vowels_on_left = 0
    evens_on_right = 0
    for i in range(len(sides) - 1):
        if sides[i] in vowels:
            vowels_on_left += 1
        if sides[i + 1] in evens:
            evens_on_right += 1
    return max(vowels_on_left, evens_on_right)

