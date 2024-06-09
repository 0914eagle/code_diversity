
def get_distant_pebble(pebble_sequence):
    # Initialize variables
    distant_pebble = 0
    current_pebble = 0
    visited_pebbles = set()

    # Iterate through the pebble sequence
    for pebble in pebble_sequence:
        # If the current pebble has not been visited before, check if it is the most distant pebble so far
        if current_pebble not in visited_pebbles:
            # If the current pebble is the most distant pebble so far, update the distant pebble
            if current_pebble > distant_pebble:
                distant_pebble = current_pebble

            # Add the current pebble to the set of visited pebbles
            visited_pebbles.add(current_pebble)

        # Increment the current pebble
        current_pebble += 1

    # Return the most distant pebble
    return distant_pebble

def main():
    # Read the input
    n = int(input())
    pebble_sequence = list(map(int, input().split()))

    # Find the most distant pebble
    distant_pebble = get_distant_pebble(pebble_sequence)

    # Print the result
    print(distant_pebble)

if __name__ == '__main__':
    main()

