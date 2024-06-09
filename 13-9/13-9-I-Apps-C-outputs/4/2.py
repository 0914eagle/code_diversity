
import itertools

def num_entirely_unsorted_sequences(arr):
    n = len(arr)
    count = 0
    for perm in itertools.permutations(arr):
        sorted_indices = [i for i, x in enumerate(perm) if x in arr]
        if len(sorted_indices) == n:
            count += 1
    return count % (10**9 + 9)

