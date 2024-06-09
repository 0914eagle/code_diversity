
def get_points(num_hands, dominant_suit, cards):
    points = 0
    suit_values = {"S": 1, "H": 2, "D": 3, "C": 4}
    dominant_suit_value = suit_values[dominant_suit]
    for card in cards:
        number = card[0]
        suit = card[1]
        if suit == dominant_suit:
            points += 11
        else:
            points += suit_values[suit]
    return points

