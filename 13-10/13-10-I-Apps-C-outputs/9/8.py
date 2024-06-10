
def get_tube_lengths(N):
    return list(map(int, input().split()))

def get_pair_of_tubes(tube_lengths, L1, L2):
    pairs = []
    for i in range(N):
        for j in range(i+1, N):
            if tube_lengths[i] + tube_lengths[j] <= L1 and tube_lengths[i+N] + tube_lengths[j+N] <= L2:
                pairs.append([tube_lengths[i], tube_lengths[j], tube_lengths[i+N], tube_lengths[j+N]])
    return pairs

def get_max_total_length(pairs):
    max_length = 0
    for pair in pairs:
        total_length = sum(pair)
        if total_length > max_length:
            max_length = total_length
    return max_length

def main():
    L1, L2, N = map(int, input().split())
    tube_lengths = get_tube_lengths(N)
    pairs = get_pair_of_tubes(tube_lengths, L1, L2)
    if not pairs:
        print("Impossible")
    else:
        print(get_max_total_length(pairs))

if __name__ == '__main__':
    main()

