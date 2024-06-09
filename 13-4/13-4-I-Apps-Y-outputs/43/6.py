
def get_points(n, b, cards):
    points = 0
    suits = ["S", "H", "D", "C"]
    suit_values = {
        "S": 11,
        "H": 4,
        "D": 3,
        "C": 2,
    }
    for card in cards:
        number = card[0]
        suit = card[1]
        if suit == b:
            points += suit_values[suit]
        else:
            points += suit_values[suit] // 2
    return points

