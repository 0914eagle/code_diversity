
def get_good_sequence(pairs):
    n = len(pairs)
    indices = list(range(1, n+1))
    sequence = []
    for i in range(n):
        sequence.append(pairs[i][0])
        sequence.append(pairs[i][1])
    sequence.sort()
    return sequence

def get_largest_subset(pairs):
    n = len(pairs)
    indices = list(range(1, n+1))
    max_subset = []
    for i in range(n):
        subset = [i]
        for j in range(i+1, n):
            if pairs[i][1] < pairs[j][0]:
                subset.append(j)
        if len(subset) > len(max_subset):
            max_subset = subset
    return max_subset

def get_index_sequence(pairs, max_subset):
    n = len(pairs)
    indices = list(range(1, n+1))
    index_sequence = []
    for i in max_subset:
        index_sequence.append(i)
    return index_sequence

def main():
    n = int(input())
    pairs = []
    for i in range(n):
        pair = list(map(int, input().split()))
        pairs.append(pair)
    sequence = get_good_sequence(pairs)
    max_subset = get_largest_subset(pairs)
    index_sequence = get_index_sequence(pairs, max_subset)
    print(len(max_subset))
    print(*index_sequence)

if __name__ == '__main__':
    main()

