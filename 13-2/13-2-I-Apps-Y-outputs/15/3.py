
def is_good_sequence(sequence):
    return all(sequence.count(x) == x for x in sequence)

def remove_elements_to_make_good(sequence):
    removed_elements = 0
    while not is_good_sequence(sequence):
        unique_elements = set(sequence)
        for element in unique_elements:
            if sequence.count(element) > element:
                removed_elements += 1
                sequence.remove(element)
                break
    return removed_elements

if __name__ == '__main__':
    n = int(input())
    sequence = list(map(int, input().split()))
    print(remove_elements_to_make_good(sequence))

