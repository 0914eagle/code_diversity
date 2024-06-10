
def calculate_points(cards):
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
    
    total_points = tablet_count**2 + compass_count**2 + gear_count**2 + 7 * min(tablet_count, compass_count, gear_count)
    return total_points

if __name__ == "__main__":
    cards = input().strip()
    points = calculate_points(cards)
    print(points)
