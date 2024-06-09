
def get_most_distant_pebble(pebble_spots):
    # Initialize variables
    most_distant_pebble = 0
    current_pebble = 0
    visited_pebbles = set()
    
    # Iterate through the pebbles
    for i in range(len(pebble_spots)):
        # Check if the current pebble has been visited before
        if current_pebble in visited_pebbles:
            continue
        
        # Check if the current pebble is the most distant pebble so far
        if i > most_distant_pebble:
            most_distant_pebble = i
        
        # Add the current pebble to the visited pebbles set
        visited_pebbles.add(current_pebble)
        
        # Check if the current pebble has any spots
        if pebble_spots[current_pebble] > 0:
            # Find the next pebble with the same number of spots
            for j in range(current_pebble + 1, len(pebble_spots)):
                if pebble_spots[current_pebble] == pebble_spots[j]:
                    current_pebble = j
                    break
        
    return most_distant_pebble

def main():
    # Read the input
    num_pebbles = int(input())
    pebble_spots = list(map(int, input().split()))
    
    # Find the most distant pebble
    most_distant_pebble = get_most_distant_pebble(pebble_spots)
    
    # Print the result
    print(most_distant_pebble)

if __name__ == '__main__':
    main()

