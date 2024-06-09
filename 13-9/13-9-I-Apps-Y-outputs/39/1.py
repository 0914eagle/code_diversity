
def get_safe_operations(registers):
    # Initialize the number of safe operations to the number of registers
    safe_operations = len(registers)
    
    # Iterate through the registers in reverse order
    for i in range(len(registers)-1, -1, -1):
        # Check if the current register is equal to the prime number corresponding to its index
        if registers[i] == [2, 3, 5, 7, 11, 13, 17, 19][i]:
            # If it is, decrement the number of safe operations
            safe_operations -= 1
    
    return safe_operations

