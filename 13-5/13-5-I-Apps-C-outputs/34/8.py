
def get_min_heights(n, m, heights):
    # Initialize the minimum height as the maximum height in the input
    min_height = max(heights)
    # Loop through each intersection and find the minimum height that satisfies the conditions
    for i in range(n):
        for j in range(m):
            # Get the height of the current intersection
            current_height = heights[i][j]
            # Find the maximum height among the heights of the skyscrapers on the same street
            max_height = max(heights[i])
            # Find the minimum height among the heights of the skyscrapers on the same street
            min_height = min(heights[i])
            # Update the minimum height if necessary
            if current_height > max_height:
                min_height = max_height
            if current_height < min_height:
                min_height = current_height
    return min_height

def main():
    n, m = map(int, input().split())
    heights = []
    for i in range(n):
        heights.append(list(map(int, input().split())))
    min_heights = get_min_heights(n, m, heights)
    for i in range(n):
        for j in range(m):
            print(min_heights[i][j], end=" ")
        print()

if __name__ == '__main__':
    main()

