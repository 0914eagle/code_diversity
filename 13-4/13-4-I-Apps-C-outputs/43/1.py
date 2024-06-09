
def get_resistors(a, b):
    # Initialize the number of resistors to 0
    num_resistors = 0
    # Initialize the current resistance to 0
    current_resistance = 0
    # While the current resistance is less than the target resistance
    while current_resistance < a:
        # Increment the number of resistors
        num_resistors += 1
        # Add the unit resistance to the current resistance
        current_resistance += 1
    # Return the number of resistors
    return num_resistors

def get_parallel_resistors(a, b):
    # Initialize the number of resistors to 0
    num_resistors = 0
    # Initialize the current resistance to 0
    current_resistance = 0
    # While the current resistance is less than the target resistance
    while current_resistance < a:
        # Increment the number of resistors
        num_resistors += 1
        # Add the unit resistance to the current resistance
        current_resistance += 1
    # Return the number of resistors
    return num_resistors

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_resistors(a, b))
    print(get_parallel_resistors(a, b))

