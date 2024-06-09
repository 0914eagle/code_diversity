
def get_bottles(shipment_volume, bottle1_volume, bottle2_volume):
    if shipment_volume > bottle1_volume or bottle1_volume < bottle2_volume:
        return "Impossible"
    
    num_bottles1 = shipment_volume // bottle1_volume
    num_bottles2 = 0
    while num_bottles1 > 0:
        num_bottles2 += 1
        num_bottles1 -= num_bottles2 * bottle2_volume
    
    return num_bottles1, num_bottles2

