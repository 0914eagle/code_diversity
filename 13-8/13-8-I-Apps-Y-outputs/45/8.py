
def get_bottles(shipment_volume, bottle1_volume, bottle2_volume):
    if bottle1_volume < bottle2_volume:
        return "Impossible"
    num_bottles1 = int(shipment_volume / bottle1_volume)
    num_bottles2 = int(shipment_volume / bottle2_volume)
    if num_bottles1 * bottle1_volume == shipment_volume and num_bottles2 * bottle2_volume == shipment_volume:
        return str(num_bottles1) + " " + str(num_bottles2)
    else:
        return "Impossible"

