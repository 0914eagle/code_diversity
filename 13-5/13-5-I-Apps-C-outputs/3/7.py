
def get_pattern(filenames, m):
    # Initialize a set to store the indices of the files to be deleted
    indices = set(m)
    # Initialize a list to store the characters of the pattern
    pattern = []
    # Loop through the filenames
    for i, filename in enumerate(filenames):
        # If the current filename is in the set of indices, add a '?' to the pattern
        if i in indices:
            pattern.append('?')
        # Otherwise, add the current character of the filename to the pattern
        else:
            pattern.append(filename[0])
    # Return the pattern as a string
    return ''.join(pattern)

def main():
    # Read the number of files and the number of files to be deleted
    n, m = map(int, input().split())
    # Read the filenames
    filenames = [input() for _ in range(n)]
    # Read the indices of the files to be deleted
    indices = set(map(int, input().split()))
    # Check if a pattern exists
    if len(indices) == m:
        # If a pattern exists, find it and print it
        pattern = get_pattern(filenames, indices)
        print("Yes")
        print(pattern)
    else:
        # If no pattern exists, print "No"
        print("No")

if __name__ == '__main__':
    main()

