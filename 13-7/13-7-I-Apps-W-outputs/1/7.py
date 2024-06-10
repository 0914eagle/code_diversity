
def get_max_candies(n, x, heights, masses):
    # Initialize variables
    max_candies = 0
    current_height = x
    current_mass = 0
    types = []

    # Iterate through the candies
    for i in range(n):
        # Check if the current candy is reachable
        if current_height >= heights[i]:
            # Add the candy to the list of reachable candies
            types.append(i)

            # Check if the current candy is of the same type as the previous candy
            if len(types) > 1 and types[-1] == types[-2]:
                # If the current candy is of the same type as the previous candy, remove the previous candy from the list
                types.pop()
            else:
                # Otherwise, update the current mass and height
                current_mass += masses[i]
                current_height += masses[i]

                # Update the maximum number of candies
                max_candies = max(max_candies, len(types))

    return max_candies

def main():
    n, x = map(int, input().split())
    heights = []
    masses = []
    for i in range(n):
        t, h, m = map(int, input().split())
        heights.append(h)
        masses.append(m)
    max_candies = get_max_candies(n, x, heights, masses)
    print(max_candies)

if __name__ == '__main__':
    main()

