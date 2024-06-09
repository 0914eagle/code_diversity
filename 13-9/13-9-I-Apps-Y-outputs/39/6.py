
def get_safe_operations(registers):
    # Convert the input list to a dictionary for easier access
    registers = dict(enumerate(registers))
    
    # Initialize the number of safe operations to the maximum value
    safe_operations = float('inf')
    
    # Iterate through the registers starting from the smallest prime
    for p in [2, 3, 5, 7, 11, 13, 17, 19]:
        # Get the current value of the register and the maximum value it can hold
        value = registers[p]
        max_value = p - 1
        
        # If the current value is equal to the maximum value, the register will overflow
        if value == max_value:
            # Decrement the number of safe operations by 1
            safe_operations -= 1
            
            # If the number of safe operations becomes negative, return 0
            if safe_operations < 0:
                return 0
            
            # Reset the register to 0 and continue with the next register
            registers[p] = 0
        else:
            # The register did not overflow, so continue with the next register
            break
    
    # Return the number of safe operations
    return safe_operations

