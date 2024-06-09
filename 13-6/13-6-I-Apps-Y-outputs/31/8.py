
def get_scientific_points(cards):
    points = 0
    tablet_count = 0
    compass_count = 0
    gear_count = 0
    for card in cards:
        if card == 'T':
            tablet_count += 1
        elif card == 'C':
            compass_count += 1
        else:
            gear_count += 1
        points += tablet_count**2 + compass_count**2 + gear_count**2
    return points

