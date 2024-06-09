
def f1(n, pebbles):
    # f1 function to find the most distant pebble that can be reached by successive jumps
    # n: number of pebbles
    # pebbles: list of numbers of spots on each pebble
    
    # Initialize variables
    max_distance = 0
    current_pebble = 0
    
    # Loop through each pebble
    for i in range(n):
        # Calculate the sum of spots on the current pebble and the next pebble
        sum_spots = pebbles[i] + pebbles[(i + 1) % n]
        
        # If the sum of spots is equal to the distance between the pebbles, update the maximum distance and current pebble
        if sum_spots == i + 1:
            max_distance = max(max_distance, i + 1)
            current_pebble = (i + 1) % n
    
    # Return the maximum distance and current pebble
    return max_distance, current_pebble

def f2(n, pebbles, max_distance, current_pebble):
    # f2 function to find the most distant pebble that can be reached by successive jumps
    # n: number of pebbles
    # pebbles: list of numbers of spots on each pebble
    # max_distance: maximum distance reached so far
    # current_pebble: current pebble
    
    # Initialize variables
    next_pebble = (current_pebble + 1) % n
    
    # If the next pebble is not the starting pebble, calculate the sum of spots on the current pebble and the next pebble
    if next_pebble != 0:
        sum_spots = pebbles[current_pebble] + pebbles[next_pebble]
        
        # If the sum of spots is equal to the distance between the pebbles, update the maximum distance and current pebble
        if sum_spots == next_pebble:
            max_distance = max(max_distance, next_pebble)
            current_pebble = next_pebble
    
    # Return the maximum distance and current pebble
    return max_distance, current_pebble

if __name__ == '__main__':
    # Read input
    n = int(input())
    pebbles = list(map(int, input().split()))
    
    # Initialize variables
    max_distance = 0
    current_pebble = 0
    
    # Find the most distant pebble that can be reached by successive jumps
    for i in range(n):
        max_distance, current_pebble = f2(n, pebbles, max_distance, current_pebble)
    
    # Print output
    print(max_distance)

