
def get_good_sequence(pairs):
    n = len(pairs)
    indices = list(range(1, n+1))
    sequence = [pairs[i-1][0] for i in indices]
    sequence += [pairs[i-1][1] for i in indices]
    return sequence

def get_largest_subset(pairs):
    n = len(pairs)
    indices = list(range(1, n+1))
    max_subset = []
    for i in indices:
        subset = [i]
        for j in indices:
            if j not in subset and pairs[i-1][0] < pairs[j-1][0] and pairs[i-1][1] > pairs[j-1][1]:
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
    max_subset = get_largest_subset(pairs)
    index_sequence = get_index_sequence(pairs, max_subset)
    print(len(max_subset))
    print(*index_sequence)

if __name__ == '__main__':
    main()

