
def get_points(n, b, cards):
    points = 0
    suits = ["S", "H", "D", "C"]
    suit_values = {
        "S": 11,
        "H": 4,
        "D": 3,
        "C": 2
    }
    for i in range(n):
        hand = cards[i * 4:(i + 1) * 4]
        hand_points = 0
        for card in hand:
            number = card[0]
            suit = card[1]
            if suit == b:
                hand_points += suit_values[suit]
            else:
                hand_points += suit_values[suit]
        points += hand_points
    return points

