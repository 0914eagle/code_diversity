
def get_bottles(shipment_volume, bottle1_volume, bottle2_volume):
    if shipment_volume > bottle1_volume or bottle1_volume < bottle2_volume:
        return "Impossible"
    
    num_bottle1 = shipment_volume // bottle1_volume
    num_bottle2 = 0
    remaining_volume = shipment_volume % bottle1_volume
    
    while remaining_volume > 0:
        if remaining_volume < bottle2_volume:
            num_bottle2 += 1
            remaining_volume = 0
        else:
            num_bottle2 += remaining_volume // bottle2_volume
            remaining_volume = remaining_volume % bottle2_volume
    
    return num_bottle1, num_bottle2

