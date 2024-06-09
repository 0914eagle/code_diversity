
def get_resistors_needed(a, b):
    # Initialize the number of resistors needed to 0
    resistors_needed = 0
    # Initialize the current resistance to 0
    current_resistance = 0
    # While the current resistance is less than the target resistance
    while current_resistance < a:
        # Increment the number of resistors needed
        resistors_needed += 1
        # Add the unit resistance to the current resistance
        current_resistance += 1
    # Return the number of resistors needed
    return resistors_needed

def get_resistors_needed_parallel(a, b):
    # Initialize the number of resistors needed to 0
    resistors_needed = 0
    # Initialize the current resistance to 0
    current_resistance = 0
    # While the current resistance is less than the target resistance
    while current_resistance < a:
        # Increment the number of resistors needed
        resistors_needed += 1
        # Add the unit resistance to the current resistance
        current_resistance += 1
    # Return the number of resistors needed
    return resistors_needed

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_resistors_needed(a, b))
    print(get_resistors_needed_parallel(a, b))

