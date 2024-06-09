
def is_good_sequence(sequence):
    return all(sequence.count(x) == x for x in sequence)

def remove_elements(sequence):
    removed_elements = 0
    while not is_good_sequence(sequence):
        sequence = [x for x in sequence if x != sequence.count(x)]
        removed_elements += 1
    return removed_elements

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    print(remove_elements(sequence))

