
def get_additional_birds(l, d, n, positions):
    # Calculate the available space for the additional birds
    available_space = l - n * d - 6

    # Sort the positions of the existing birds
    sorted_positions = sorted(positions)

    # Initialize the number of additional birds as the available space
    additional_birds = available_space

    # Iterate through the positions of the existing birds
    for i in range(n - 1):
        # Calculate the distance between the current bird and the next bird
        distance = sorted_positions[i + 1] - sorted_positions[i]

        # Check if the distance is less than the minimum distance between birds
        if distance < d:
            # Calculate the number of additional birds that can fit between the current bird and the next bird
            additional_birds_between = int((d - distance) / d)

            # Update the number of additional birds
            additional_birds -= additional_birds_between

    # Return the number of additional birds that can sit on the wire
    return additional_birds

def main():
    l, d, n = map(int, input().split())
    positions = list(map(int, input().split()))
    print(get_additional_birds(l, d, n, positions))

if __name__ == '__main__':
    main()

