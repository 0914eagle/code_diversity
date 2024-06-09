
def f1(n, pebbles):
    # f1(n, pebbles) should return the most distant pebble that can be reached by a sequence of jumps
    # according to the given rules
    
    # Initialize the most distant pebble as the first pebble
    most_distant_pebble = 0
    
    # Iterate through the list of pebbles
    for i in range(1, n):
        # If the sum of the number of spots on the current pebble and the previous pebble is equal to the distance between them,
        # then the current pebble is a valid jump
        if pebbles[i] + pebbles[i-1] == i:
            # Update the most distant pebble if the current pebble is farther away than the previous one
            most_distant_pebble = max(most_distant_pebble, i)
    
    return most_distant_pebble

def f2(n, pebbles):
    # f2(n, pebbles) should return the number of different pairs of pebbles where Yoshi can perform a jump
    # according to the given rules
    
    # Initialize the number of pairs as 0
    num_pairs = 0
    
    # Iterate through the list of pebbles
    for i in range(n-1):
        # If the sum of the number of spots on the current pebble and the next pebble is equal to the distance between them,
        # then the current pebble and the next pebble form a valid jump
        if pebbles[i] + pebbles[i+1] == i+1:
            # Increment the number of pairs
            num_pairs += 1
    
    return num_pairs

if __name__ == '__main__':
    n = int(input())
    pebbles = list(map(int, input().split()))
    print(f1(n, pebbles))

