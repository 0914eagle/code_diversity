
def get_scientific_points(cards):
    points = 0
    card_counts = {}
    for card in cards:
        if card not in card_counts:
            card_counts[card] = 1
        else:
            card_counts[card] += 1
    for card, count in card_counts.items():
        points += count ** 2
    for card in card_counts:
        if card_counts[card] == 3:
            points += 7
    return points

