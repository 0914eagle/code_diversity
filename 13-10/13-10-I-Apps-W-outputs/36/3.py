
def is_liked(s):
    # Check if the string contains the substring "one" or "two"
    if "one" in s or "two" in s:
        return False
    return True

def find_min_removals(s):
    # Initialize variables
    removals = 0
    indices_to_remove = []

    # Iterate over the string
    for i in range(len(s)):
        # Check if the current character is "o" or "t"
        if s[i] == "o" or s[i] == "t":
            # Check if the next character is "n"
            if i + 1 < len(s) and s[i + 1] == "n":
                # Check if the next two characters are "e" and "o"
                if i + 2 < len(s) and s[i + 2] == "e" and s[i + 3] == "o":
                    # Add the current index to the list of indices to remove
                    indices_to_remove.append(i)
                    removals += 1

    # Return the minimum number of removals and the list of indices to remove
    return removals, indices_to_remove

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        s = input()

        # Check if the string is liked
        if is_liked(s):
            print("0")
        else:
            # Find the minimum number of removals
            removals, indices_to_remove = find_min_removals(s)

            # Print the minimum number of removals and the list of indices to remove
            print(removals)
            print(" ".join(map(str, indices_to_remove)))

if __name__ == '__main__':
    main()

