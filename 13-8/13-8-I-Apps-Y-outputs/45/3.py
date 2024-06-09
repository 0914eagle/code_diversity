
def solve_problem(shipment_volume, bottle1_volume, bottle2_volume):
    if shipment_volume <= 0 or bottle1_volume <= 0 or bottle2_volume <= 0:
        return "Impossible"
    if bottle1_volume < bottle2_volume:
        bottle1_volume, bottle2_volume = bottle2_volume, bottle1_volume
    num_bottles1 = shipment_volume // bottle1_volume
    num_bottles2 = 0
    while num_bottles1 * bottle1_volume + num_bottles2 * bottle2_volume < shipment_volume:
        num_bottles2 += 1
    if num_bottles1 * bottle1_volume + num_bottles2 * bottle2_volume == shipment_volume:
        return str(num_bottles1) + " " + str(num_bottles2)
    else:
        return "Impossible"

