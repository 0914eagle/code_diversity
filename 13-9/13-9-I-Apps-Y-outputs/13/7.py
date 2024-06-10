
def is_power_of_two(n):
    return n > 0 and not n & (n - 1)

def is_good_sequence(sequence):
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if is_power_of_two(sequence[i] + sequence[j]):
                return True
    return False

def get_min_elements_to_remove(sequence):
    min_elements_to_remove = len(sequence)
    for i in range(len(sequence)):
        current_sequence = sequence[:i] + sequence[i + 1:]
        if is_good_sequence(current_sequence):
            min_elements_to_remove = min(min_elements_to_remove, len(sequence) - len(current_sequence))
    return min_elements_to_remove

if __name__ == '__main__':
    n = int(input())
    sequence = [int(x) for x in input().split()]
    print(get_min_elements_to_remove(sequence))

