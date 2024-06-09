
def f1(l, d, n, positions):
    # Calculate the available space for the additional birds
    available_space = l - n * d - 6

    # Sort the positions of the birds
    sorted_positions = sorted(positions)

    # Initialize the number of additional birds that can sit
    additional_birds = 0

    # Iterate through the positions of the birds
    for i in range(n - 1):
        # Calculate the distance between the current bird and the next bird
        distance = sorted_positions[i + 1] - sorted_positions[i]

        # Check if the distance is greater than the available space
        if distance > available_space:
            # If the distance is greater than the available space, no additional birds can sit
            return additional_birds
        else:
            # If the distance is less than or equal to the available space, calculate the number of additional birds that can sit
            additional_birds += 1

    # Return the number of additional birds that can sit
    return additional_birds

def f2(l, d, n, positions):
    # Calculate the available space for the additional birds
    available_space = l - n * d - 6

    # Sort the positions of the birds
    sorted_positions = sorted(positions)

    # Initialize the number of additional birds that can sit
    additional_birds = 0

    # Iterate through the positions of the birds
    for i in range(n - 1):
        # Calculate the distance between the current bird and the next bird
        distance = sorted_positions[i + 1] - sorted_positions[i]

        # Check if the distance is greater than the available space
        if distance > available_space:
            # If the distance is greater than the available space, no additional birds can sit
            return additional_birds
        else:
            # If the distance is less than or equal to the available space, calculate the number of additional birds that can sit
            additional_birds += 1

    # Return the number of additional birds that can sit
    return additional_birds

if __name__ == '__main__':
    l, d, n = map(int, input().split())
    positions = list(map(int, input().split()))
    print(f1(l, d, n, positions))
    print(f2(l, d, n, positions))

