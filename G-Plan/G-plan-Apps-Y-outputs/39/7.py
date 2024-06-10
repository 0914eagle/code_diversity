
def calculate_points(cards):
    tablet_count = cards.count('T')
    compass_count = cards.count('C')
    gear_count = cards.count('G')
    
    total_points = tablet_count**2 + compass_count**2 + gear_count**2 + 7 * min(tablet_count, compass_count, gear_count)
    
    return total_points

if __name__ == "__main__":
    cards = input().strip()
    points = calculate_points(cards)
    print(points)
