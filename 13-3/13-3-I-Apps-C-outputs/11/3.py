
import itertools

def get_entirely_unsorted_sequences(numbers):
    n = len(numbers)
    unsorted_sequences = 0
    for perm in itertools.permutations(numbers):
        sorted_indices = [i for i in range(n) if perm[i] == i]
        if len(sorted_indices) == 0:
            unsorted_sequences += 1
    return unsorted_sequences % (10**9 + 9)

