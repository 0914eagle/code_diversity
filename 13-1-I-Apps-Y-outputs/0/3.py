
def get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume):
    if large_bottle_volume < small_bottle_volume:
        return "Impossible"
    
    large_bottles = shipment_volume // large_bottle_volume
    small_bottles = (shipment_volume - large_bottles * large_bottle_volume) // small_bottle_volume
    
    if large_bottles + small_bottles < shipment_volume:
        return "Impossible"
    
    return large_bottles, small_bottles

