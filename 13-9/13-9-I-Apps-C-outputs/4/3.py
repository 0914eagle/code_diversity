
import itertools

def get_unsorted_sequences(arr):
    n = len(arr)
    count = 0
    for perm in itertools.permutations(arr):
        sorted_arr = sorted(perm)
        if sorted_arr == perm:
            count += 1
    return count % (10**9 + 9)

