
def get_potential_friends(n, m, k, armies):
    # Initialize a set to store the potential friends
    potential_friends = set()

    # Iterate over the armies
    for i in range(m):
        # Get the binary representation of the current army
        binary_representation = list(bin(armies[i])[2:])

        # Iterate over the armies again
        for j in range(m):
            # If the current army is not the same as the current army, check if they are potential friends
            if i != j:
                # Get the binary representation of the current army
                binary_representation_j = list(bin(armies[j])[2:])

                # Count the number of different bits between the two armies
                different_bits = 0
                for bit in range(n):
                    if binary_representation[bit] != binary_representation_j[bit]:
                        different_bits += 1

                # If the number of different bits is less than or equal to k, add the current player to the set of potential friends
                if different_bits <= k:
                    potential_friends.add(j + 1)

    # Return the number of potential friends
    return len(potential_friends)

def main():
    # Read the input
    n, m, k = map(int, input().split())
    armies = []
    for i in range(m):
        armies.append(int(input()))

    # Call the function to get the number of potential friends
    potential_friends = get_potential_friends(n, m, k, armies)

    # Print the result
    print(potential_friends)

if __name__ == '__main__':
    main()

