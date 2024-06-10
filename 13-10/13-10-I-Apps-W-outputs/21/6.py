
def get_max_groups(n, m):
    # Initialize a list to store the positions of the cats that have left the circle
    left_cats = []
    
    # Iterate through the number of cats that have left the circle
    for i in range(m):
        # Add the position of the cat that has left the circle to the list
        left_cats.append(i)
    
    # Initialize a variable to store the maximum number of groups
    max_groups = 0
    
    # Iterate through the number of cats that are still in the circle
    for i in range(n - m):
        # Check if the current cat's position is in the list of cats that have left the circle
        if i not in left_cats:
            # If it is not, increment the maximum number of groups
            max_groups += 1
    
    # Return the maximum number of groups
    return max_groups

def main():
    n, m = map(int, input().split())
    print(get_max_groups(n, m))

if __name__ == '__main__':
    main()

