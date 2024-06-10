
def get_max_groups(n, m):
    # Calculate the number of cats that are left in the circle
    num_cats_left = n - m
    
    # Calculate the number of groups that can be formed
    num_groups = num_cats_left
    
    # Return the maximum number of groups
    return num_groups
    
def main():
    # Read the input data
    n, m = map(int, input().split())
    
    # Calculate the maximum number of groups
    max_groups = get_max_groups(n, m)
    
    # Print the result
    print(max_groups)
    
if __name__ == '__main__':
    main()

