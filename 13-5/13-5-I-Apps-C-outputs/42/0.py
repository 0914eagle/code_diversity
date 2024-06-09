
def f1(n, pebbles):
    # f1 function to find the most distant pebble that can be reached by a sequence of jumps
    # n: number of pebbles
    # pebbles: list of numbers of spots on each pebble
    
    # Initialize variables
    max_distance = 0
    current_pebble = 0
    
    # Iterate through each pebble
    for i in range(n):
        # Check if the current pebble can be reached by a jump from the previous pebble
        if pebbles[current_pebble] + pebbles[i] == i - current_pebble:
            # Update the maximum distance and the current pebble
            max_distance = max(max_distance, i - current_pebble)
            current_pebble = i
    
    # Return the maximum distance
    return max_distance

def f2(n, pebbles):
    # f2 function to find all possible pairs of pebbles where Yoshi can perform a jump
    # n: number of pebbles
    # pebbles: list of numbers of spots on each pebble
    
    # Initialize a list to store the pairs of pebbles
    pairs = []
    
    # Iterate through each pebble
    for i in range(n):
        # Iterate through each pebble after the current pebble
        for j in range(i+1, n):
            # Check if the current pebble can be reached by a jump from the previous pebble
            if pebbles[i] + pebbles[j] == j - i:
                # Add the pair of pebbles to the list
                pairs.append((i, j))
    
    # Return the list of pairs
    return pairs

if __name__ == '__main__':
    # Read the input
    n = int(input())
    pebbles = list(map(int, input().split()))
    
    # Find the most distant pebble that can be reached by a sequence of jumps
    max_distance = f1(n, pebbles)
    
    # Find all possible pairs of pebbles where Yoshi can perform a jump
    pairs = f2(n, pebbles)
    
    # Print the output
    print(max_distance)

