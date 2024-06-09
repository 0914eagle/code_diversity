
def get_max_strength(n, p, assignment):
    # Initialize the maximum strength and the optimal prefix or suffix
    max_strength = 0
    opt_prefix_or_suffix = ""

    # Iterate over all possible prefixes or suffixes
    for i in range(n):
        # Get the strength of the pieces in the current prefix or suffix
        curr_strength = sum(p[i:i+n])

        # If the current strength is greater than the maximum strength, update the maximum strength and the optimal prefix or suffix
        if curr_strength > max_strength:
            max_strength = curr_strength
            opt_prefix_or_suffix = assignment[i:i+n]

    # Return the maximum strength and the optimal prefix or suffix
    return max_strength, opt_prefix_or_suffix

def main():
    # Read the input
    n = int(input())
    p = list(map(int, input().split()))
    assignment = input()

    # Get the maximum strength and the optimal prefix or suffix
    max_strength, opt_prefix_or_suffix = get_max_strength(n, p, assignment)

    # Print the maximum strength
    print(max_strength)

if __name__ == '__main__':
    main()

