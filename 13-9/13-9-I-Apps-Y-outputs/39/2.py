
def get_safe_operations(registers):
    # Initialize the number of safe operations to the number of registers
    safe_operations = len(registers)
    
    # Iterate through the registers from last to first
    for i in range(len(registers)-1, -1, -1):
        # If the current register is not zero, break the loop
        if registers[i] != 0:
            break
        # Otherwise, decrement the number of safe operations
        safe_operations -= 1
    
    return safe_operations

