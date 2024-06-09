
def javelin_length(n, lengths):
    total_length = 0
    for length in lengths:
        total_length += length
        total_length -= 1
    return total_length

