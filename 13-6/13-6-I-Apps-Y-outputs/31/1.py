
def get_scientific_points(cards):
    points = 0
    card_count = {}
    for card in cards:
        if card not in card_count:
            card_count[card] = 1
        else:
            card_count[card] += 1
    for card, count in card_count.items():
        points += count ** 2
    for card in card_count:
        if card_count[card] == 3:
            points += 7
    return points

