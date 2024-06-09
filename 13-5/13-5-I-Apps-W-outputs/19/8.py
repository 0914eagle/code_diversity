
def get_good_sequences(n, a):
    def bitwise_xor(a, b):
        return a ^ b

    def get_good_sequence(sequence):
        return all(bitwise_xor(a, b) == 0 for a, b in zip(sequence, sequence[1:]))

    def count_good_sequences(n, a):
        count = 0
        for l in range(n):
            for r in range(l, n):
                if get_good_sequence(a[l:r+1]):
                    count += 1
        return count

    return count_good_sequences(n, a)

