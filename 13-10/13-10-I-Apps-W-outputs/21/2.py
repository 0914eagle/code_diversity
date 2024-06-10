
def divide_into_groups(n, m):
    # Initialize a list to store the positions of the cats that have left the circle
    left_cats = []
    
    # Iterate through the number of cats that have left the circle
    for i in range(m):
        # Take the last cat that has left the circle and add it to the list of left cats
        left_cats.append(n - i)
    
    # Initialize a variable to store the maximum number of groups
    max_groups = 0
    
    # Iterate through the list of left cats
    for i in range(len(left_cats)):
        # Check if the current cat has not been considered yet
        if i not in left_cats:
            # Initialize a variable to store the number of groups
            num_groups = 0
            
            # Iterate through the list of left cats
            for j in range(len(left_cats)):
                # Check if the current cat has not been considered yet and if it is next to the current cat
                if j not in left_cats and (left_cats[i] + 1) % n == left_cats[j] or (left_cats[i] - 1) % n == left_cats[j]:
                    # Increment the number of groups
                    num_groups += 1
                    
                    # Add the current cat to the list of considered cats
                    left_cats.append(left_cats[j])
            
            # Check if the number of groups is greater than the current maximum
            if num_groups > max_groups:
                # Update the maximum number of groups
                max_groups = num_groups
    
    # Return the maximum number of groups
    return max_groups

def main():
    # Read the input
    n, m = map(int, input().split())
    
    # Call the divide_into_groups function and print the result
    print(divide_into_groups(n, m))

if __name__ == '__main__':
    main()

