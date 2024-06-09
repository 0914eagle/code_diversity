
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
        elif card == 'G':
            gear_count += 1
    points += tablet_count * tablet_count
    points += compass_count * compass_count
    points += gear_count * gear_count
    if tablet_count + compass_count + gear_count >= 3:
        points += 7
    return points

