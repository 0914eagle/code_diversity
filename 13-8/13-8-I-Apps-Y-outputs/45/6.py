
def solve_problem(shipment_volume, large_bottle_volume, small_bottle_volume):
    # Check if the shipment volume is greater than the volume of the large bottles
    if shipment_volume > large_bottle_volume:
        return "Impossible"
    
    # Calculate the number of large bottles needed to hold the shipment volume
    num_large_bottles = shipment_volume // large_bottle_volume
    
    # Calculate the remaining volume that cannot be held by the large bottles
    remaining_volume = shipment_volume % large_bottle_volume
    
    # Calculate the number of small bottles needed to hold the remaining volume
    num_small_bottles = remaining_volume // small_bottle_volume
    
    # Return the number of large and small bottles needed
    return num_large_bottles, num_small_bottles

