
def compare_cards(card1, card2):
    card_values = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13
    }
    card1_value = card_values[card1]
    card2_value = card_values[card2]
    if card1_value > card2_value:
        return "Alice"
    elif card1_value < card2_value:
        return "Bob"
    else:
        return "Draw"

card1, card2 = map(int, input().split())
print(compare_cards(card1, card2))

