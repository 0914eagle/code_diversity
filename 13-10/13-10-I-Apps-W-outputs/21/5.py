
def count_groups(n, m):
    # Initialize a list to store the positions of the cats that have left
    left_cats = []
    
    # Iterate through the number of cats that have left
    for i in range(m):
        # Add the position of the cat that has left to the list
        left_cats.append(i)
    
    # Initialize a variable to store the maximum number of groups
    max_groups = 0
    
    # Iterate through the number of cats that are still at the party
    for i in range(n):
        # Check if the current cat has left the party
        if i not in left_cats:
            # If the current cat has not left, increment the maximum number of groups
            max_groups += 1
    
    # Return the maximum number of groups
    return max_groups

def main():
    # Read the input from stdin
    n, m = map(int, input().split())
    
    # Call the count_groups function and print the result
    print(count_groups(n, m))

if __name__ == '__main__':
    main()

