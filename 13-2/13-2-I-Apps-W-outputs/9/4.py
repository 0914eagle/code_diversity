
def f1(n, x):
    # Initialize variables
    ice_cream = x
    distressed_kids = 0
    
    # Iterate through the queue
    for i in range(n):
        # Read the next operation
        operation = input().split()
        
        # If the operation is a carrier, take all the ice cream
        if operation[0] == "+":
            ice_cream += int(operation[1])
        
        # If the operation is a child, give the child ice cream if possible
        elif operation[0] == "-":
            if ice_cream >= int(operation[1]):
                ice_cream -= int(operation[1])
            else:
                distressed_kids += 1
    
    # Return the number of ice cream packs left and the number of distressed kids
    return ice_cream, distressed_kids

