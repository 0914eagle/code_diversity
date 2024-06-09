
import itertools

def get_entirely_unsorted_sequences(numbers):
    num_sequences = 0
    for perm in itertools.permutations(numbers):
        is_sorted = True
        for i in range(len(perm) - 1):
            if perm[i] > perm[i + 1]:
                is_sorted = False
                break
        if not is_sorted:
            num_sequences += 1
    return num_sequences % (10**9 + 9)

