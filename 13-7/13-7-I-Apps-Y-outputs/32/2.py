
def frequency_sorter(sequence, k):
    
    # Initialize a dictionary to store the frequency of each element
    freq = {}
    for elem in sequence:
        if elem not in freq:
            freq[elem] = 0
        freq[elem] += 1

    # Sort the dictionary by frequency and value
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    # Create the sorted sequence
    sorted_seq = []
    for elem, count in sorted_freq:
        sorted_seq += [elem] * count

    return sorted_seq

