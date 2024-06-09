
def get_safe_operations(registers):
    # Initialize the number of safe operations to the number of registers
    safe_operations = len(registers)
    
    # Iterate through the registers in reverse order
    for i in range(len(registers)-1, -1, -1):
        # Check if the current register is equal to its maximum value
        if registers[i] == i:
            # If the current register is equal to its maximum value, set it to 0 and decrement the next register
            registers[i] = 0
            registers[i-1] += 1
        # Check if the current register is not equal to its maximum value
        else:
            # If the current register is not equal to its maximum value, break the loop
            break
    
    # Return the number of safe operations
    return safe_operations - registers[0]

