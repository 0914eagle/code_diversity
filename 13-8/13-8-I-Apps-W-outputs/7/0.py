
def get_possible_options(n, x, y, z, a):
    # Initialize the number of possible options to 0
    options = 0
    
    # Iterate over each castle and calculate the number of possible options for each castle
    for i in range(n):
        # Calculate the number of possible options for the current castle
        options += calculate_options(i, x, y, z, a)
    
    # Return the total number of possible options
    return options

def calculate_options(i, x, y, z, a):
    # Initialize the number of possible options to 0
    options = 0
    
    # If the current castle has at least one alive defender, calculate the number of possible options
    if a[i] > 0:
        # Calculate the number of possible options for a mixed attack
        options += calculate_options_mixed(i, x, y, z, a)
        
        # Calculate the number of possible options for an infantry attack
        options += calculate_options_infantry(i, x, y, z, a)
        
        # Calculate the number of possible options for a cavalry attack
        options += calculate_options_cavalry(i, x, y, z, a)
    
    # Return the number of possible options
    return options

def calculate_options_mixed(i, x, y, z, a):
    # Initialize the number of possible options to 0
    options = 0
    
    # If the current castle has at least x alive defenders, calculate the number of possible options
    if a[i] >= x:
        # Calculate the number of possible options for a mixed attack
        options += 1
    
    # Return the number of possible options
    return options

def calculate_options_infantry(i, x, y, z, a):
    # Initialize the number of possible options to 0
    options = 0
    
    # If the current castle has at least y alive defenders and the previous attack was not an infantry attack, calculate the number of possible options
    if a[i] >= y and a[i-1] != y:
        # Calculate the number of possible options for an infantry attack
        options += 1
    
    # Return the number of possible options
    return options

def calculate_options_cavalry(i, x, y, z, a):
    # Initialize the number of possible options to 0
    options = 0
    
    # If the current castle has at least z alive defenders and the previous attack was not a cavalry attack, calculate the number of possible options
    if a[i] >= z and a[i-1] != z:
        # Calculate the number of possible options for a cavalry attack
        options += 1
    
    # Return the number of possible options
    return options

def main():
    # Read the input
    t = int(input())
    for i in range(t):
        n, x, y, z = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Calculate the number of possible options for the first attack
        options = get_possible_options(n, x, y, z, a)
        
        # Print the number of possible options
        print(options)

if __name__ == '__main__':
    main()

