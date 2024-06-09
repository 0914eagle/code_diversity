
def f1(n, pebbles):
    # f1(n, pebbles) should return the most distant pebble that can be reached by a sequence of jumps
    # according to the given rules and starting from the first pebble
    
    # Initialize the most distant pebble as the first pebble
    most_distant_pebble = 0
    
    # Iterate through the pebbles starting from the second pebble
    for i in range(1, n):
        # If the sum of the number of spots on the current pebble and the previous pebble is equal to the distance between them,
        # update the most distant pebble
        if pebbles[i] + pebbles[i-1] == i - most_distant_pebble:
            most_distant_pebble = i
    
    # Return the most distant pebble
    return most_distant_pebble

def f2(n, pebbles):
    # f2(n, pebbles) should return the number of pairs of pebbles where Yoshi can perform a jump from one pebble to another one
    # during his sequence of jumps
    
    # Initialize a counter for the number of pairs
    num_pairs = 0
    
    # Iterate through the pebbles
    for i in range(n-1):
        # If the sum of the number of spots on the current pebble and the next pebble is equal to the distance between them,
        # increment the counter
        if pebbles[i] + pebbles[i+1] == 1:
            num_pairs += 1
    
    # Return the number of pairs
    return num_pairs

if __name__ == '__main__':
    n = int(input())
    pebbles = list(map(int, input().split()))
    print(f1(n, pebbles))

