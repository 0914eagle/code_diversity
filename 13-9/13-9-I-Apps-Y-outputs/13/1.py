
def is_good_sequence(sequence):
    for i in range(len(sequence)):
        for j in range(i+1, len(sequence)):
            if (sequence[i] + sequence[j]) & (sequence[i] + sequence[j] - 1) == 0:
                return True
    return False

def get_min_elements_to_remove(sequence):
    count = 0
    for i in range(len(sequence)):
        if not is_good_sequence(sequence[:i] + sequence[i+1:]):
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    print(get_min_elements_to_remove(sequence))

