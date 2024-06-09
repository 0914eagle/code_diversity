
def get_max_strength(n, p, assignment):
    # Initialize variables
    max_strength = 0
    prefix_suffix = ""

    # Iterate over all possible prefixes and suffixes
    for i in range(n):
        for j in range(i, n):
            # Calculate the strength of the pieces in the prefix and suffix
            prefix_strength = sum(p[k] for k in range(i))
            suffix_strength = sum(p[k] for k in range(j, n))

            # Calculate the total strength of the pieces in the prefix and suffix
            total_strength = prefix_strength + suffix_strength

            # If the total strength is greater than the current maximum strength, update the maximum strength and the prefix and suffix
            if total_strength > max_strength:
                max_strength = total_strength
                prefix_suffix = (i, j)

    # Return the maximum strength and the prefix and suffix with the maximum strength
    return max_strength, prefix_suffix

def flip_prefix_suffix(n, p, assignment, prefix_suffix):
    # Initialize variables
    prefix_strength = 0
    suffix_strength = 0
    flipped_assignment = ""

    # Get the prefix and suffix with the maximum strength
    prefix_index, suffix_index = prefix_suffix

    # Iterate over the pieces in the prefix and suffix
    for i in range(n):
        # If the piece is in the prefix, calculate its strength and add it to the prefix strength
        if i < prefix_index:
            prefix_strength += p[i]
        # If the piece is in the suffix, calculate its strength and add it to the suffix strength
        elif i >= suffix_index:
            suffix_strength += p[i]

    # Iterate over the pieces in the prefix and suffix
    for i in range(n):
        # If the piece is in the prefix, flip its assignment and add it to the flipped assignment
        if i < prefix_index:
            flipped_assignment += "B" if assignment[i] == "A" else "A"
        # If the piece is in the suffix, flip its assignment and add it to the flipped assignment
        elif i >= suffix_index:
            flipped_assignment += "B" if assignment[i] == "A" else "A"

    # Return the flipped assignment
    return flipped_assignment

def main():
    # Read the input
    n = int(input())
    p = list(map(int, input().split()))
    assignment = input()

    # Get the maximum strength and the prefix and suffix with the maximum strength
    max_strength, prefix_suffix = get_max_strength(n, p, assignment)

    # Flip the prefix and suffix with the maximum strength
    flipped_assignment = flip_prefix_suffix(n, p, assignment, prefix_suffix)

    # Print the maximum strength and the flipped assignment
    print(max_strength)
    print(flipped_assignment)

if __name__ == '__main__':
    main()

