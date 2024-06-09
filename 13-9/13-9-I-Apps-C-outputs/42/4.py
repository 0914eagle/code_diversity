
def is_divisibility_hack_valid(b, d):
    # Initialize a set to store the remainders
    remainders = set()
    
    # Iterate from 1 to b-1
    for i in range(1, b):
        # Calculate the remainder of i divided by d
        remainder = i % d
        
        # If the remainder is already in the set, return "no"
        if remainder in remainders:
            return "no"
        
        # Add the remainder to the set
        remainders.add(remainder)
    
    # If we reach this point, return "yes"
    return "yes"

