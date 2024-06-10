
def calculate_points(input_str):
    tablet_count = input_str.count('T')
    compass_count = input_str.count('C')
    gear_count = input_str.count('G')
    
    total_points = tablet_count**2 + compass_count**2 + gear_count**2 + 7 * min(tablet_count, compass_count, gear_count)
    
    return total_points

if __name__ == "__main__":
    input_str = input().strip()
    print(calculate_points(input_str))
