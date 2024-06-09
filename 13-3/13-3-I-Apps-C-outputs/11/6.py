
import itertools

def get_entirely_unsorted_sequences(numbers):
    n = len(numbers)
    sequences = []
    for perm in itertools.permutations(numbers):
        sorted_indices = [i for i, x in enumerate(perm) if x == numbers[i]]
        if len(sorted_indices) == 0:
            sequences.append(perm)
    return len(sequences) % (10**9 + 9)

