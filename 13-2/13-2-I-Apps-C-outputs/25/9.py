
def get_valid_segments(affection_values, k):
    total = 0
    valid_segments = 0
    for i in range(len(affection_values)):
        total += affection_values[i]
        if total == k:
            valid_segments += 1
        elif total > k:
            break
    return valid_segments

