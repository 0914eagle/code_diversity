
def longest_consecutive_subsequence(sequence, start_index, subset):
    max_length = 0
    current_length = 0
    for i in range(start_index, len(sequence)):
        if sequence[i] in subset:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    return max(max_length, current_length)

