
def get_max_birds(l, d, n, positions):
    # Sort the positions of the birds
    sorted_positions = sorted(positions)

    # Initialize the number of additional birds that can sit on the wire
    max_birds = 0

    # Iterate over the positions of the birds
    for i in range(n):
        # Check if the current position is at least 6 cm from the poles
        if sorted_positions[i] >= 6:
            # Check if the current position is at least d cm from the previous bird
            if i == 0 or sorted_positions[i] - sorted_positions[i - 1] >= d:
                # Increment the number of additional birds that can sit on the wire
                max_birds += 1

    return max_birds

def main():
    l, d, n = map(int, input().split())
    positions = []
    for _ in range(n):
        positions.append(int(input()))
    print(get_max_birds(l, d, n, positions))

if __name__ == '__main__':
    main()

