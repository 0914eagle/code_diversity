
def get_maximum(sequence):
    maximum = -float('inf')
    for i in range(len(sequence)):
        maximum = max(maximum, max(sequence[:i] + sequence[i+1:]))
    return maximum

