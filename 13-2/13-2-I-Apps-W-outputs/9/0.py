
def f1(n, x):
    # Initialize variables
    ice_cream = x
    distressed_kids = 0
    
    # Iterate through the queue
    for i in range(n):
        # Read the next operation
        operation, amount = input().split()
        amount = int(amount)
        
        # If the operation is to give ice cream, give it to the child
        if operation == "-":
            if ice_cream >= amount:
                ice_cream -= amount
            else:
                distressed_kids += 1
                ice_cream = 0
        # If the operation is to take ice cream, take it from the carrier
        elif operation == "+":
            ice_cream += amount
    
    # Return the number of ice cream packs left and the number of distressed kids
    return ice_cream, distressed_kids

