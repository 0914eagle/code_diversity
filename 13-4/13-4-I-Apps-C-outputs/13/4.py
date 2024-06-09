
def smallest_different_sequence(r, m):
    sequence = [r]
    n = 1
    while m not in sequence:
        d = 1
        while d in sequence:
            d += 1
        sequence.append(sequence[n-1] + d)
        n += 1
    return n

