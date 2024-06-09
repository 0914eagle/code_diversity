
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
    for card1, card2, card3 in combinations(card_counts, 3):
        if card1 != card2 and card1 != card3 and card2 != card3:
            points += 7
    return points

