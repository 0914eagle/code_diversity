
def javelin_length(rods):
    total_length = 0
    for rod in rods:
        total_length += rod
        total_length -= 1
    return total_length

