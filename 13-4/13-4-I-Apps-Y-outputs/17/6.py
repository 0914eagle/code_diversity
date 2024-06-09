
def javelin_length(rod_lengths):
    total_length = 0
    for rod_length in rod_lengths:
        total_length += rod_length
        total_length -= 1
    return total_length

