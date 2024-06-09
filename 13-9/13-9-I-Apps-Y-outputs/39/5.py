
def get_safe_operations(registers):
    # Initialize the number of safe operations to the number of registers
    safe_operations = len(registers)
    
    # Iterate through the registers in reverse order
    for i in range(len(registers)-1, -1, -1):
        # If the current register is 1, the computer will blow up
        if registers[i] == 1:
            return 0
        # If the current register is not 1, decrement the number of safe operations
        else:
            safe_operations -= 1
    
    return safe_operations

