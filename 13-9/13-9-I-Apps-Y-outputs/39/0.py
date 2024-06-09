
def get_safe_operations(registers):
    # Convert the input list to a dictionary for easier access
    registers = dict(enumerate(registers))
    
    # Initialize the number of safe operations to the maximum value
    safe_operations = 19
    
    # Iterate through the registers starting from the smallest prime
    for p in [2, 3, 5, 7, 11, 13, 17, 19]:
        # Get the current value of the register
        value = registers[p]
        
        # If the value is not zero, decrement it and break the loop
        if value != 0:
            registers[p] = value - 1
            break
        
        # If the value is zero, increment the number of safe operations
        safe_operations -= 1
    
    # Return the number of safe operations
    return safe_operations

