
def is_good_sequence(sequence):
    return all(sequence.count(x) == x for x in sequence)

def solve(sequence):
    if is_good_sequence(sequence):
        return 0
    for i in range(len(sequence)):
        sequence_copy = sequence[:i] + sequence[i+1:]
        if is_good_sequence(sequence_copy):
            return 1
    return len(sequence)

if __name__ == '__main__':
    sequence_length = int(input())
    sequence = tuple(map(int, input().split()))
    print(solve(sequence))

