
def longest_sequence(intervals):
    sequences = []
    for i in range(len(intervals)):
        sequence = [intervals[i]]
        for j in range(i+1, len(intervals)):
            if intervals[j][0] <= sequence[-1][1]:
                sequence.append(intervals[j])
        sequences.append(sequence)
    return max(sequences, key=len)

