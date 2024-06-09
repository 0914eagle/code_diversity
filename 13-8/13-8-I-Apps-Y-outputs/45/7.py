
def get_bottles(shipment_volume, bottle1_volume, bottle2_volume):
    if shipment_volume <= 0 or bottle1_volume <= 0 or bottle2_volume <= 0:
        return "Impossible"
    if bottle1_volume < bottle2_volume:
        bottle1_volume, bottle2_volume = bottle2_volume, bottle1_volume
    num_bottles1 = shipment_volume // bottle1_volume
    num_bottles2 = 0
    while num_bottles1 > 0:
        remaining_volume = shipment_volume - num_bottles1 * bottle1_volume
        if remaining_volume % bottle2_volume == 0:
            num_bottles2 = remaining_volume // bottle2_volume
            break
        num_bottles1 -= 1
    if num_bottles1 == 0:
        return "Impossible"
    return num_bottles1, num_bottles2

