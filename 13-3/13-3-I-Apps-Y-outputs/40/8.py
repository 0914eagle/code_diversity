
def get_max_value(sequence):
    max_value = -float('inf')
    for i in range(len(sequence)):
        current_value = sequence[i]
        other_values = sequence[:i] + sequence[i+1:]
        max_value = max(max_value, max(other_values))
    return max_value

