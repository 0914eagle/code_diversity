
def f1(n, pebbles):
    # f1(n, pebbles) should return the most distant pebble that can be reached by a sequence of jumps
    # starting from the first pebble and following the given rules
    
    # Initialize the most distant pebble as the first pebble
    most_distant_pebble = 0
    
    # Iterate through the list of pebbles
    for i in range(1, n):
        # Check if the sum of the number of spots on the current pebble and the previous pebble is equal to the distance between them
        if pebbles[i] + pebbles[i-1] == i:
            # If it is, update the most distant pebble
            most_distant_pebble = i
    
    # Return the most distant pebble
    return most_distant_pebble

def f2(n, pebbles):
    # f2(n, pebbles) should return the number of pairs of pebbles where Yoshi can perform a jump
    # from one pebble to another one during his sequence of jumps
    
    # Initialize a counter for the number of pairs
    num_pairs = 0
    
    # Iterate through the list of pebbles
    for i in range(n-1):
        # Check if the sum of the number of spots on the current pebble and the next pebble is equal to the distance between them
        if pebbles[i] + pebbles[i+1] == i+1:
            # If it is, increment the counter
            num_pairs += 1
    
    # Return the number of pairs
    return num_pairs

if __name__ == '__main__':
    # Read the input
    n = int(input())
    pebbles = list(map(int, input().split()))
    
    # Call f1 and f2
    most_distant_pebble = f1(n, pebbles)
    num_pairs = f2(n, pebbles)
    
    # Print the output
    print(most_distant_pebble)

