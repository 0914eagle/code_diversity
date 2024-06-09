
def solve(n, m):
    def is_wool_sequence(sequence):
        for i in range(len(sequence)):
            for j in range(i+1, len(sequence)):
                if sequence[i] ^ sequence[j] == 0:
                    return True
        return False

    def count_non_wool_sequences(n, m):
        count = 0
        for i in range(1 << n):
            sequence = [j for j in range(n) if (i & (1 << j)) != 0]
            if not is_wool_sequence(sequence):
                count += 1
        return count

    return count_non_wool_sequences(n, m) % 1000000009

