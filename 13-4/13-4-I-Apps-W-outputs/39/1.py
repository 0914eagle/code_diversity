
def f1(l, d, n, positions):
    # Calculate the available space for the additional birds
    available_space = l - (n * d) - (2 * 6)

    # Return the maximum number of additional birds that can sit on the wire
    return available_space // d

def f2(l, d, n, positions):
    # Initialize the number of additional birds as 0
    additional_birds = 0

    # Sort the positions of the birds in ascending order
    sorted_positions = sorted(positions)

    # Iterate through the positions of the birds
    for i in range(n):
        # Calculate the distance between the current bird and the next bird
        distance = sorted_positions[i + 1] - sorted_positions[i]

        # If the distance is greater than or equal to the minimum distance between birds, increase the number of additional birds
        if distance >= d:
            additional_birds += 1

    # Return the number of additional birds that can sit on the wire
    return additional_birds

if __name__ == '__main__':
    l, d, n = map(int, input().split())
    positions = list(map(int, input().split()))
    print(f1(l, d, n, positions))
    print(f2(l, d, n, positions))

