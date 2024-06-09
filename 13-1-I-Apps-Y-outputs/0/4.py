
def get_bottles(shipment_volume, large_bottle_volume, small_bottle_volume):
    if large_bottle_volume < small_bottle_volume or shipment_volume <= 0:
        return "Impossible"
    
    large_bottles = shipment_volume // large_bottle_volume
    small_bottles = 0
    remaining_volume = shipment_volume % large_bottle_volume
    
    while remaining_volume > 0 and small_bottles < large_bottles:
        if remaining_volume >= small_bottle_volume:
            small_bottles += 1
            remaining_volume -= small_bottle_volume
        else:
            break
    
    return str(large_bottles) + " " + str(small_bottles)

