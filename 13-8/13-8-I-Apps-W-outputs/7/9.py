
def get_options_for_first_attack(n, x, y, z, a):
    # Initialize a list to store the options for the first attack
    options = []
    
    # Iterate over each castle and check if it can be targeted by the White King
    for i in range(n):
        # Check if the castle has at least one defender
        if a[i] > 0:
            # Check if the castle has not been attacked before
            if i not in options:
                # Add the castle to the list of options
                options.append(i)
    
    # Return the list of options for the first attack
    return options

def get_number_of_options(n, x, y, z, a):
    # Get the options for the first attack
    options = get_options_for_first_attack(n, x, y, z, a)
    
    # Initialize a variable to store the number of options
    num_options = 0
    
    # Iterate over each option and check if it allows the White King to launch the last attack
    for i in options:
        # Check if the castle has at least one defender
        if a[i] > 0:
            # Check if the castle has not been attacked before
            if i not in options:
                # Add the castle to the list of options
                num_options += 1
    
    # Return the number of options for the first attack that allow the White King to launch the last attack
    return num_options

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x, y, z = map(int, input().split())
        a = list(map(int, input().split()))
        print(get_number_of_options(n, x, y, z, a))

