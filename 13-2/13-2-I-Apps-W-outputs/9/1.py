
def f1(n, x):
    # Initialize variables
    ice_cream = x
    distressed_kids = 0
    
    # Iterate through the queue
    for i in range(n):
        # Read the next operation
        operation = input().split()
        
        # If the operation is "+", a carrier has arrived
        if operation[0] == "+":
            # Add the number of ice cream packs to the total
            ice_cream += int(operation[1])
        
        # If the operation is "-", a child has arrived
        elif operation[0] == "-":
            # Try to give the child the requested number of ice cream packs
            if ice_cream >= int(operation[1]):
                # If there are enough ice cream packs, give them to the child
                ice_cream -= int(operation[1])
            else:
                # If there are not enough ice cream packs, the child goes away distressed
                distressed_kids += 1
    
    # Return the number of ice cream packs left and the number of distressed kids
    return ice_cream, distressed_kids

