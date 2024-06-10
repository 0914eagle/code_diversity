
def get_groups(n, m):
    # Initialize a list to store the positions of the cats that have left
    left_cats = []
    
    # Iterate through the number of cats that have left
    for i in range(m):
        # Remove a cat from the list of cats at the party
        left_cats.append(n)
        n -= 1
    
    # Initialize a variable to store the maximum number of groups
    max_groups = 0
    
    # Iterate through the list of cats that have left
    for i in range(len(left_cats)):
        # Check if the current cat has been removed from the list of cats at the party
        if left_cats[i] in left_cats:
            # If so, remove the current cat from the list of cats at the party
            left_cats.remove(left_cats[i])
            # Increment the maximum number of groups
            max_groups += 1
    
    # Return the maximum number of groups
    return max_groups

def main():
    # Test the get_groups function with example inputs
    n, m = 7, 4
    print(get_groups(n, m))
    n, m = 6, 2
    print(get_groups(n, m))
    n, m = 3, 0
    print(get_groups(n, m))
    n, m = 2, 2
    print(get_groups(n, m))

if __name__ == '__main__':
    main()

