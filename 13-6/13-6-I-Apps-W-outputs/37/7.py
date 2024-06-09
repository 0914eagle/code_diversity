
def get_potential_friends(n, m, k, armies):
    # Initialize a set to store the potential friends
    potential_friends = set()
    
    # Iterate over the armies
    for i in range(m):
        # Get the binary representation of the ith army
        binary_rep = list(bin(armies[i])[2:])
        # Iterate over the jth bit of the ith army
        for j in range(n):
            # If the jth bit is 1, add the ith player to the potential friends set
            if binary_rep[j] == "1":
                potential_friends.add(i)
    
    # Return the number of potential friends
    return len(potential_friends)

def main():
    # Read the input
    n, m, k = map(int, input().split())
    armies = []
    for i in range(m + 1):
        armies.append(int(input()))
    
    # Call the get_potential_friends function and print the result
    print(get_potential_friends(n, m, k, armies))

if __name__ == '__main__':
    main()

