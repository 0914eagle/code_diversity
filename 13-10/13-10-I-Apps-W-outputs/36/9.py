
def get_min_removals(s):
    # Initialize variables
    removals = 0
    indices_to_remove = []

    # Iterate through the string
    for i in range(len(s)):
        # Check if the substring "one" or "two" is present
        if s[i:i+3] in ["one", "two"]:
            # If it is, add it to the list of indices to remove
            indices_to_remove.append(i)
            removals += 1

    # Return the minimum number of removals and the list of indices to remove
    return removals, indices_to_remove

def get_output(s, removals, indices_to_remove):
    # Initialize the output string
    output = ""

    # Iterate through the string
    for i in range(len(s)):
        # Check if the current index is in the list of indices to remove
        if i in indices_to_remove:
            # If it is, skip it
            continue
        # If it's not, add the current character to the output string
        output += s[i]

    # Return the output string
    return output

if __name__ == '__main__':
    # Read the input
    t = int(input())
    for _ in range(t):
        s = input()

        # Get the minimum number of removals and the list of indices to remove
        removals, indices_to_remove = get_min_removals(s)

        # Get the output string
        output = get_output(s, removals, indices_to_remove)

        # Print the output
        print(removals)
        print(" ".join(map(str, indices_to_remove)))

