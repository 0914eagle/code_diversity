
def get_army_types(x):
    # Convert x to binary and count the number of ones
    return bin(x).count("1")

def get_potential_friends(n, m, k, armies):
    # Initialize a set to store the potential friends
    potential_friends = set()

    # Iterate over the armies
    for i in range(m):
        # Get the number of types of soldiers in the current army
        num_types = get_army_types(armies[i])

        # Iterate over the remaining armies
        for j in range(i + 1, m):
            # Get the number of types of soldiers in the current army
            num_types_j = get_army_types(armies[j])

            # Check if the number of types of soldiers differ by at most k
            if abs(num_types - num_types_j) <= k:
                # Add the current player to the set of potential friends
                potential_friends.add(i + 1)
                potential_friends.add(j + 1)

    # Return the number of potential friends
    return len(potential_friends)

def main():
    # Read the input
    n, m, k = map(int, input().split())
    armies = [int(input()) for _ in range(m)]

    # Call the function to get the number of potential friends
    num_potential_friends = get_potential_friends(n, m, k, armies)

    # Print the result
    print(num_potential_friends)

if __name__ == '__main__':
    main()

