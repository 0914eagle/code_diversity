
def get_maximum(sequence):
    result = []
    for i in range(len(sequence)):
        other_elements = sequence[:i] + sequence[i+1:]
        result.append(max(other_elements))
    return result

