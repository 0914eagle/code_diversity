
def get_tube_lengths(N):
    tube_lengths = []
    for i in range(N):
        tube_lengths.append(int(input()))
    return tube_lengths

def get_max_total_length(tube_lengths, L1, L2):
    max_total_length = 0
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            if tube_lengths[i] + tube_lengths[j] <= L1 and tube_lengths[i+j] + tube_lengths[j+1] <= L2:
                max_total_length = max(max_total_length, tube_lengths[i] + tube_lengths[j] + tube_lengths[i+j] + tube_lengths[j+1])
    if max_total_length == 0:
        return "Impossible"
    else:
        return max_total_length

def main():
    L1, L2, N = map(int, input().split())
    tube_lengths = get_tube_lengths(N)
    print(get_max_total_length(tube_lengths, L1, L2))

if __name__ == '__main__':
    main()

