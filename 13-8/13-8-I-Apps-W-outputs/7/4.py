
def get_possible_options(n, x, y, z, a):
    # Initialize the number of possible options to 0
    possible_options = 0
    
    # Iterate over each castle and calculate the number of possible options for each castle
    for i in range(n):
        # Calculate the number of possible options for the current castle
        possible_options_current_castle = 0
        
        # If the current castle has at least one defender, calculate the number of possible options for the current castle
        if a[i] > 0:
            # Calculate the number of possible options for a mixed attack
            possible_options_mixed = (a[i] - 1) // x + 1
            
            # Calculate the number of possible options for an infantry attack
            possible_options_infantry = (a[i] - 1) // y + 1
            
            # Calculate the number of possible options for a cavalry attack
            possible_options_cavalry = (a[i] - 1) // z + 1
            
            # Calculate the total number of possible options for the current castle
            possible_options_current_castle = possible_options_mixed + possible_options_infantry + possible_options_cavalry
        
        # Add the number of possible options for the current castle to the total number of possible options
        possible_options += possible_options_current_castle
    
    # Return the total number of possible options
    return possible_options

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate over each test case
    for i in range(t):
        # Read the input for the current test case
        n, x, y, z = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Calculate the number of possible options for the White King's first attack
        possible_options = get_possible_options(n, x, y, z, a)
        
        # Print the number of possible options for the White King's first attack
        print(possible_options)

if __name__ == '__main__':
    main()

