
def get_total_segments(affection_values, k):
    total_segments = 0
    for i in range(len(affection_values)):
        for j in range(i, len(affection_values)):
            total_affection = sum(affection_values[i:j+1])
            if total_affection >= 0 and total_affection % k == 0:
                total_segments += 1
    return total_segments

