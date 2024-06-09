
def get_pebble_sequence(n, pebbles):
    # Initialize a list to store the pebbles and the current pebble index
    pebble_sequence = [0]
    current_pebble_index = 0
    
    # Iterate through the pebbles
    for i in range(1, n):
        # Get the current pebble and the previous pebble
        current_pebble = pebbles[i]
        previous_pebble = pebbles[current_pebble_index]
        
        # Check if the sum of the spots on the current and previous pebbles is equal to the distance between them
        if current_pebble + previous_pebble == i:
            # If it is, add the current pebble to the sequence and update the current pebble index
            pebble_sequence.append(current_pebble)
            current_pebble_index = i
    
    return pebble_sequence

def get_most_distant_pebble(pebble_sequence):
    # Get the last pebble in the sequence
    last_pebble = pebble_sequence[-1]
    
    # Return the distance between the last pebble and the first pebble
    return last_pebble

if __name__ == '__main__':
    n = int(input())
    pebbles = list(map(int, input().split()))
    pebble_sequence = get_pebble_sequence(n, pebbles)
    most_distant_pebble = get_most_distant_pebble(pebble_sequence)
    print(most_distant_pebble)

