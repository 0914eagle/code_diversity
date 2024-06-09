
def smallest_different_sequence(A1, m):
    sequence = [A1]
    n = 1
    while m not in sequence:
        d = get_next_difference(sequence)
        sequence.append(sequence[n-1] + d)
        n += 1
    return n

def get_next_difference(sequence):
    used_numbers = set(sequence)
    for i in range(1, len(sequence)):
        if i not in used_numbers:
            return i
    return len(sequence) + 1

print(smallest_different_sequence(1, 5))
print(smallest_different_sequence(1, 12))

