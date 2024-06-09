
def get_min_knights_to_remove(knights, colors, counts):
    # Initialize a dictionary to store the counts of each color
    color_counts = {color: 0 for color in range(1, len(colors) + 1)}
    
    # Iterate through the knights and increment the count of their color
    for knight, color in zip(knights, colors):
        color_counts[color] += 1
    
    # Initialize the minimum number of knights to remove to be the total number of knights
    min_knights_to_remove = len(knights)
    
    # Iterate through the colors and check if the desired count can be achieved
    for color, count in counts.items():
        # If the desired count is greater than the actual count, we cannot achieve it
        if count > color_counts[color]:
            return -1
        # If the desired count is less than the actual count, we can remove the excess knights
        elif count < color_counts[color]:
            min_knights_to_remove = min(min_knights_to_remove, color_counts[color] - count)
    
    return min_knights_to_remove

def main():
    n, m = map(int, input().split())
    knights = list(map(int, input().split()))
    counts = {int(color): int(count) for color, count in zip(input().split(), input().split())}
    print(get_min_knights_to_remove(knights, counts))

if __name__ == '__main__':
    main()

