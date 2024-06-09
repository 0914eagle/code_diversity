
def get_safe_operations(registers):
    # Initialize a list to store the prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    
    # Initialize a variable to store the number of safe operations
    safe_operations = 0
    
    # Iterate through the registers and calculate the number of safe operations for each register
    for i in range(len(registers)):
        # Calculate the maximum value that the register can hold
        max_value = primes[i] - 1
        
        # If the current value of the register is less than the maximum value, increment the safe operations count
        if registers[i] < max_value:
            safe_operations += 1
        # If the current value of the register is equal to the maximum value, reset the register to 0 and decrement the safe operations count
        else:
            registers[i] = 0
            safe_operations -= 1
    
    # Return the number of safe operations
    return safe_operations

