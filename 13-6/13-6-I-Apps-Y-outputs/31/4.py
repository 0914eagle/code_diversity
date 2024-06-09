
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
    sets = [(card_counts['T'], card_counts['C'], card_counts['G']), (card_counts['C'], card_counts['G'], card_counts['T']), (card_counts['G'], card_counts['T'], card_counts['C'])]
    for set in sets:
        if sum(set) == 3:
            points += 7
    return points

