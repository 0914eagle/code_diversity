
def f1(n, x):
    # Initialize variables
    ice_cream_packs = x
    distressed_kids = 0
    
    # Iterate through the queue
    for i in range(n):
        # If the current person is a carrier, take all their ice cream packs
        if i % 2 == 0:
            ice_cream_packs += int(input())
        # If the current person is a child, give them ice cream packs if possible, otherwise mark them as distressed
        else:
            if ice_cream_packs >= int(input()):
                ice_cream_packs -= int(input())
            else:
                distressed_kids += 1
    
    # Return the number of ice cream packs left and the number of distressed kids
    return ice_cream_packs, distressed_kids

