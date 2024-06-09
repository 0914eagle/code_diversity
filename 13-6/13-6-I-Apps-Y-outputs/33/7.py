
def frequency_sorter(message, C):
    # Convert the message to a dictionary, where each key is a number and each value is its frequency
    frequency = {}
    for num in message:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Sort the dictionary by frequency in descending order, and then by value in ascending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))

    # Return the sorted sequence
    return [num for num, _ in sorted_frequency]

