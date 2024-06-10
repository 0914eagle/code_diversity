
def is_liked(s):
    # Check if the string contains the substring "one" or "two"
    if "one" in s or "two" in s:
        return False
    return True

def get_min_removals(s):
    # Initialize variables
    removals = 0
    indices = []

    # Check if the string is liked
    if is_liked(s):
        return removals, indices

    # Check if the string contains the substring "one"
    if "one" in s:
        # Get the index of the first occurrence of "one"
        i = s.index("one")

        # Add the index to the list of indices
        indices.append(i)

        # Remove the substring "one" from the string
        s = s[:i] + s[i+3:]

        # Increment the number of removals
        removals += 1

    # Check if the string contains the substring "two"
    if "two" in s:
        # Get the index of the first occurrence of "two"
        i = s.index("two")

        # Add the index to the list of indices
        indices.append(i)

        # Remove the substring "two" from the string
        s = s[:i] + s[i+3:]

        # Increment the number of removals
        removals += 1

    # Return the minimum number of removals and the list of indices
    return removals, indices

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate over the test cases
    for i in range(num_test_cases):
        # Read the input string
        s = input()

        # Get the minimum number of removals and the list of indices
        removals, indices = get_min_removals(s)

        # Print the output
        print(removals)
        print(" ".join(map(str, indices)))

if __name__ == '__main__':
    main()

