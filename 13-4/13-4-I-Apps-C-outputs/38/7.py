
def get_distant_pebble(pebbles):
    # Initialize the distant pebble as the first pebble
    distant_pebble = 0
    # Initialize the current pebble as the first pebble
    current_pebble = 0
    # Iterate through the list of pebbles
    for i in range(1, len(pebbles)):
        # If the sum of the number of spots on the current pebble and the previous pebble is equal to the distance between them, then we can jump from the current pebble to the previous pebble
        if pebbles[current_pebble] + pebbles[current_pebble - 1] == i:
            # Update the distant pebble as the current pebble
            distant_pebble = current_pebble
        # Increment the current pebble
        current_pebble += 1
    # Return the distance of the distant pebble
    return distant_pebble

def main():
    # Read the number of pebbles and the list of pebbles from stdin
    n = int(input())
    pebbles = list(map(int, input().split()))
    # Call the get_distant_pebble function and print the result
    print(get_distant_pebble(pebbles))

if __name__ == '__main__':
    main()

