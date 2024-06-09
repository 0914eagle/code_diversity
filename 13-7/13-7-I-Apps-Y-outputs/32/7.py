
def frequency_sorter(sequence, C):
    # Convert the sequence to a dictionary, where each key is a number and its value is the frequency of that number
    frequency = {}
    for num in sequence:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Sort the sequence based on the frequency of each number
    sorted_sequence = sorted(sequence, key=lambda x: (-frequency[x], x))
    
    return sorted_sequence

