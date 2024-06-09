
def get_max_value(sequence):
    max_values = []
    for i in range(len(sequence)):
        other_values = sequence[:i] + sequence[i+1:]
        max_values.append(max(other_values))
    return max_values

