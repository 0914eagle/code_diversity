
def get_possible_options(n, x, y, z, a):
    # Initialize a list to store the possible options
    options = []
    
    # Iterate over each castle
    for i in range(n):
        # Check if the castle has at least one soldier
        if a[i] > 0:
            # Add the castle and the mixed attack option to the list
            options.append((i, "mixed"))
            # Add the castle and the infantry attack option to the list
            options.append((i, "infantry"))
            # Add the castle and the cavalry attack option to the list
            options.append((i, "cavalry"))
    
    # Return the list of possible options
    return options

def get_last_attacker(n, x, y, z, a):
    # Initialize a variable to store the number of possible options
    num_options = 0
    
    # Get the possible options for the first attack
    options = get_possible_options(n, x, y, z, a)
    
    # Iterate over each option
    for option in options:
        # Get the castle and the attack type
        castle, attack_type = option
        
        # Check if the attack type is mixed
        if attack_type == "mixed":
            # Decrease the number of defenders in the castle by x
            a[castle] -= x
        # Check if the attack type is infantry
        elif attack_type == "infantry":
            # Decrease the number of defenders in the castle by y
            a[castle] -= y
        # Check if the attack type is cavalry
        elif attack_type == "cavalry":
            # Decrease the number of defenders in the castle by z
            a[castle] -= z
        
        # Check if the number of defenders in the castle is now zero
        if a[castle] == 0:
            # Increment the number of possible options
            num_options += 1
    
    # Return the number of possible options
    return num_options

def main():
    # Read the number of test cases
    t = int(input())
    
    # Iterate over each test case
    for _ in range(t):
        # Read the input
        n, x, y, z = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Get the number of possible options for the White King
        options = get_last_attacker(n, x, y, z, a)
        
        # Print the number of possible options
        print(options)

if __name__ == '__main__':
    main()

