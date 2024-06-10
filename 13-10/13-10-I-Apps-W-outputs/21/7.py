
def get_maximum_groups(n, m):
    # Initialize a list to store the position of the cats that have left
    left_cats = []

    # Iterate through the number of cats that have left
    for i in range(m):
        # Get the position of the cat that has left
        left_cat = int(input())

        # Add the position of the cat to the list of left cats
        left_cats.append(left_cat)

    # Sort the list of left cats in ascending order
    left_cats.sort()

    # Initialize a variable to store the maximum number of groups
    max_groups = 0

    # Iterate through the number of cats that are still in the circle
    for i in range(n - m):
        # Get the position of the current cat
        current_cat = i + 1

        # Check if the current cat has left the circle
        if current_cat not in left_cats:
            # If the current cat has not left the circle, increment the number of groups
            max_groups += 1

    # Return the maximum number of groups
    return max_groups

def main():
    # Read the input n and m from stdin
    n, m = map(int, input().split())

    # Call the get_maximum_groups function and store the result in a variable
    max_groups = get_maximum_groups(n, m)

    # Print the result
    print(max_groups)

if __name__ == '__main__':
    main()

