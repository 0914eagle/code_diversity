
def get_tube_lengths(N):
    tube_lengths = []
    for _ in range(N):
        tube_lengths.append(int(input()))
    return tube_lengths

def get_max_total_length(tube_lengths, L1, L2):
    tube_lengths.sort(reverse=True)
    total_length = 0
    for i in range(2):
        total_length += tube_lengths[i]
        if total_length > L1:
            return "Impossible"
    for i in range(2, 4):
        total_length += tube_lengths[i]
        if total_length > L2:
            return "Impossible"
    return total_length

def main():
    L1, L2, N = map(int, input().split())
    tube_lengths = get_tube_lengths(N)
    print(get_max_total_length(tube_lengths, L1, L2))

if __name__ == '__main__':
    main()

