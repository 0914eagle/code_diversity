
def get_tube_lengths(n):
    return [int(input()) for _ in range(n)]

def get_possible_tubes(tube_lengths, L1, L2):
    possible_tubes = []
    for i in range(len(tube_lengths)):
        for j in range(i+1, len(tube_lengths)):
            if tube_lengths[i] + tube_lengths[j] <= L1 and tube_lengths[i] + tube_lengths[j] <= L2:
                possible_tubes.append([tube_lengths[i], tube_lengths[j]])
    return possible_tubes

def get_max_tube_length(possible_tubes):
    max_length = 0
    for tube1, tube2 in possible_tubes:
        max_length = max(max_length, tube1 + tube2)
    return max_length

def main():
    L1, L2, N = map(int, input().split())
    tube_lengths = get_tube_lengths(N)
    possible_tubes = get_possible_tubes(tube_lengths, L1, L2)
    if possible_tubes:
        print(get_max_tube_length(possible_tubes))
    else:
        print("Impossible")

if __name__ == '__main__':
    main()

