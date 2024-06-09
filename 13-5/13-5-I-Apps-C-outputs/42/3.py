
def f1(n, spots):
    # Initialize a dictionary to store the distances of each pebble from the first pebble
    distances = {0: 0}
    
    # Iterate through the list of spots
    for i in range(n):
        # Get the current pebble's spot number
        current_spot = spots[i]
        
        # Iterate through the previous pebbles
        for j in range(i):
            # Get the previous pebble's spot number
            previous_spot = spots[j]
            
            # Check if the current pebble's spot number is equal to the sum of the previous pebble's spot number and the distance between the two pebbles
            if current_spot == previous_spot + i - j:
                # If it is, update the distance of the current pebble from the first pebble
                distances[i] = max(distances[i], distances[j] + 1)
    
    # Return the maximum distance of any pebble from the first pebble
    return max(distances.values())

def f2(n, spots):
    # Initialize a dictionary to store the distances of each pebble from the first pebble
    distances = {0: 0}
    
    # Iterate through the list of spots
    for i in range(n):
        # Get the current pebble's spot number
        current_spot = spots[i]
        
        # Iterate through the previous pebbles
        for j in range(i):
            # Get the previous pebble's spot number
            previous_spot = spots[j]
            
            # Check if the current pebble's spot number is equal to the sum of the previous pebble's spot number and the distance between the two pebbles
            if current_spot == previous_spot + i - j:
                # If it is, update the distance of the current pebble from the first pebble
                distances[i] = max(distances[i], distances[j] + 1)
    
    # Return the maximum distance of any pebble from the first pebble
    return max(distances.values())

if __name__ == '__main__':
    n = int(input())
    spots = list(map(int, input().split()))
    print(f1(n, spots))
    print(f2(n, spots))

