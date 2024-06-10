
def set_healths(N, S):
    # Initialize a list to store the healths of the slimes
    healths = [0]
    
    # Loop through each generation of slimes
    for i in range(N):
        # Determine the number of slimes that will be spawned in this generation
        num_slimes = 2**i
        
        # Loop through each slime in this generation
        for j in range(num_slimes):
            # Set the health of the slime to be the sum of the healths of its parent slimes
            health = sum(healths[-num_slimes:])
            
            # Add the health of the slime to the list of healths
            healths.append(health)
    
    # Return True if the multiset of the healths is equal to S, False otherwise
    return multiset(healths) == multiset(S)

def multiset(lst):
    # Convert the list to a dictionary, where each key is an element in the list and each value is its frequency
    d = {}
    for elem in lst:
        if elem in d:
            d[elem] += 1
        else:
            d[elem] = 1
    
    # Return the dictionary as a multiset
    return d

if __name__ == '__main__':
    # Read the input from stdin
    N = int(input())
    S = list(map(int, input().split()))
    
    # Call the set_healths function and print the result
    result = set_healths(N, S)
    print("Yes" if result else "No")

