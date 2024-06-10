
def get_maximum_number_of_chests(n, m, a, b):
    # Initialize a dictionary to store the number of chests that can be opened using each key
    key_to_chest_count = {}

    # Iterate over the keys
    for i in range(m):
        # Initialize a set to store the chests that can be opened using the current key
        chest_set = set()

        # Iterate over the chests
        for j in range(n):
            # Check if the current key can be used to open the current chest
            if (a[j] + b[i]) % 2 == 1:
                # Add the current chest to the set
                chest_set.add(j)

        # Add the set to the dictionary
        key_to_chest_count[i] = chest_set

    # Initialize a variable to store the maximum number of chests that can be opened
    max_chest_count = 0

    # Iterate over the keys
    for i in range(m):
        # Get the set of chests that can be opened using the current key
        chest_set = key_to_chest_count[i]

        # Check if the current key can open any chest
        if len(chest_set) > 0:
            # Add the number of chests that can be opened using the current key to the maximum number of chests
            max_chest_count += len(chest_set)

    # Return the maximum number of chests that can be opened
    return max_chest_count

def main():
    # Read the input
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Call the function to get the maximum number of chests that can be opened
    max_chest_count = get_maximum_number_of_chests(n, m, a, b)

    # Print the maximum number of chests that can be opened
    print(max_chest_count)

if __name__ == '__main__':
    main()

