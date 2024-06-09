
def get_number_of_unsorted_sequences(sequence):
    n = len(sequence)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if sequence[i] > sequence[j] or sequence[j] > sequence[k]:
                    count += 1
    return count % (10**9 + 9)

