
def get_min_knights_to_remove(knights, colors, desired_counts):
    # Initialize a dictionary to store the counts of each color
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 0
    
    # Iterate through the knights and increment the count of each color
    for knight in knights:
        color_counts[knight] += 1
    
    # Initialize a variable to store the minimum number of knights to remove
    min_knights_to_remove = float('inf')
    
    # Iterate through the colors and check if the desired count is met
    for color, desired_count in desired_counts.items():
        if color_counts[color] > desired_count:
            min_knights_to_remove = min(min_knights_to_remove, color_counts[color] - desired_count)
    
    # Return the minimum number of knights to remove
    return min_knights_to_remove

def main():
    n, m = map(int, input().split())
    knights = list(map(int, input().split()))
    desired_counts = {int(color): int(count) for color, count in zip(input().split(), input().split())}
    print(get_min_knights_to_remove(knights, desired_counts.keys(), desired_counts.values()))

if __name__ == '__main__':
    main()

