
def get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume):
    if large_bottle_volume < small_bottle_volume or shipment_volume <= 0:
        return "Impossible"
    
    large_bottles = shipment_volume // large_bottle_volume
    small_bottles = (shipment_volume - large_bottles * large_bottle_volume) // small_bottle_volume
    
    if large_bottles + small_bottles < shipment_volume:
        large_bottles += 1
    
    return large_bottles, small_bottles

