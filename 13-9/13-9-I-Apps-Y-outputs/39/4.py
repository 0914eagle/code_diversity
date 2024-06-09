
def get_safe_operations(registers):
    # Initialize the number of safe operations to the number of registers
    safe_operations = len(registers)
    
    # Iterate through the registers from largest to smallest
    for i in range(len(registers)-1, -1, -1):
        # If the register is not zero, decrement the number of safe operations
        if registers[i] != 0:
            safe_operations -= 1
        # If the register is zero and the previous register is not zero, break the loop
        elif i > 0 and registers[i-1] != 0:
            break
    
    return safe_operations

