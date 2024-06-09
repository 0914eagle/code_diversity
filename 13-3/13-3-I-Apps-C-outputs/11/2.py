
import itertools

def get_entirely_unsorted_sequences(arr):
    n = len(arr)
    count = 0
    for perm in itertools.permutations(arr):
        sorted_indices = [i for i in range(n) if perm[i] == i]
        if len(sorted_indices) == 0:
            count += 1
    return count % (10**9 + 9)

