
def get_safe_operations(registers):
    # Initialize a list to store the primes
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    
    # Initialize a variable to store the number of safe operations
    safe_operations = len(registers)
    
    # Iterate over the registers and primes
    for i, (register, prime) in enumerate(zip(registers, primes)):
        # If the register is equal to the prime minus 1, the computer will blow up
        if register == prime - 1:
            # Return the number of safe operations
            return safe_operations - i - 1
    
    # If the computer has not blown up, return the number of safe operations
    return safe_operations

