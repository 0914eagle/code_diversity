
def get_minimum_knights(knights, colors, counts):
    # Initialize a dictionary to store the counts of each color
    color_counts = {color: 0 for color in range(1, len(colors) + 1)}
    
    # Initialize a variable to store the minimum number of knights to remove
    min_knights = 0
    
    # Iterate through the knights and count the number of each color
    for knight, color in zip(knights, colors):
        color_counts[color] += 1
    
    # Check if the current counts match the desired counts
    if all(color_counts[color] == count for color, count in counts.items()):
        return min_knights
    
    # If the current counts do not match, remove the knight with the most frequent color and recalculate the counts
    else:
        min_knights += 1
        color_counts[max(color_counts, key=color_counts.get)] -= 1
        return get_minimum_knights(knights[1:], colors[1:], counts)

def main():
    n, m = map(int, input().split())
    knights = list(map(int, input().split()))
    counts = {int(color): int(count) for color, count in zip(input().split(), input().split())}
    print(get_minimum_knights(knights, knights, counts))

if __name__ == '__main__':
    main()

