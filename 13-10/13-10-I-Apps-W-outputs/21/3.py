
def get_max_groups(n, m):
    # Initialize a list to store the positions of the cats that have left the circle
    left_cats = []
    
    # Iterate through the number of cats that have left the circle
    for i in range(m):
        # Choose a random cat that has left the circle
        left_cat = random.randint(1, n)
        
        # Add the position of the cat to the list of left cats
        left_cats.append(left_cat)
    
    # Initialize a list to store the groups of cats
    groups = []
    
    # Iterate through the number of cats at the party
    for i in range(n):
        # Check if the current cat has left the circle
        if i not in left_cats:
            # If the current cat has not left the circle, add it to the current group
            groups[-1].append(i)
        else:
            # If the current cat has left the circle, start a new group
            groups.append([i])
    
    # Return the maximum number of groups
    return max(len(group) for group in groups)

def main():
    n, m = map(int, input().split())
    print(get_max_groups(n, m))

if __name__ == '__main__':
    main()

