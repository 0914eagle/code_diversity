
def get_good_sequence(pairs):
    # Sort the pairs in non-decreasing order of the first element
    sorted_pairs = sorted(pairs, key=lambda x: x[0])
    # Initialize the good sequence with the first pair
    good_sequence = [sorted_pairs[0]]
    # Iterate over the remaining pairs
    for pair in sorted_pairs[1:]:
        # If the current pair is in the good sequence, skip it
        if pair in good_sequence:
            continue
        # If the current pair is not in the good sequence, add it to the end of the sequence
        good_sequence.append(pair)
    return good_sequence

def get_largest_subset(pairs):
    # Get the good sequence for the given pairs
    good_sequence = get_good_sequence(pairs)
    # Initialize the largest subset with the first pair
    largest_subset = [good_sequence[0]]
    # Iterate over the remaining pairs
    for pair in good_sequence[1:]:
        # If the current pair is not in the largest subset, add it to the end of the subset
        if pair not in largest_subset:
            largest_subset.append(pair)
    return largest_subset

def get_index_sequence(pairs, subset):
    # Get the indexes of the pairs in the subset
    index_sequence = [pairs.index(pair) for pair in subset]
    return index_sequence

def main():
    n = int(input())
    pairs = []
    for i in range(n):
        a, b = map(int, input().split())
        pairs.append((a, b))
    largest_subset = get_largest_subset(pairs)
    index_sequence = get_index_sequence(pairs, largest_subset)
    print(len(largest_subset))
    print(*index_sequence)

if __name__ == '__main__':
    main()

