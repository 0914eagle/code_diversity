
def javelin_length(steel_rods):
    total_length = 0
    for rod in steel_rods:
        total_length += rod
        total_length -= 1
    return total_length

