
def get_possible_options(n, x, y, z, a):
    # Initialize the number of possible options to 0
    possible_options = 0
    
    # Iterate through each castle and calculate the number of possible options for each castle
    for i in range(n):
        # If the castle has at least one soldier, calculate the number of possible options for the castle
        if a[i] > 0:
            # Calculate the number of possible options for a mixed attack
            mixed_options = a[i] // x
            
            # Calculate the number of possible options for an infantry attack
            infantry_options = a[i] // y
            
            # Calculate the number of possible options for a cavalry attack
            cavalry_options = a[i] // z
            
            # Add the number of possible options for each type of attack to the total number of possible options
            possible_options += mixed_options + infantry_options + cavalry_options
    
    # Return the total number of possible options
    return possible_options

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate through each test case
    for i in range(t):
        # Read the input for the test case
        n, x, y, z = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Calculate the number of possible options for the first attack
        possible_options = get_possible_options(n, x, y, z, a)
        
        # Print the number of possible options for the first attack
        print(possible_options)

if __name__ == '__main__':
    main()

