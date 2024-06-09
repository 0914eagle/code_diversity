
def get_min_mp(N, A, B, C, lengths):
    # Initialize the minimum MP needed to achieve the objective
    min_mp = 0

    # Sort the lengths in non-decreasing order
    sorted_lengths = sorted(lengths)

    # Use Extension Magic to obtain the bamboo of length A
    while sorted_lengths[0] < A:
        min_mp += 1
        sorted_lengths[0] += 1

    # Use Composition Magic to obtain the bamboo of length B
    while sorted_lengths[0] + sorted_lengths[1] < B:
        min_mp += 10
        sorted_lengths[0] += sorted_lengths[1]
        sorted_lengths.pop(1)

    # Use Shortening Magic to obtain the bamboo of length C
    while sorted_lengths[-1] > C:
        min_mp += 1
        sorted_lengths[-1] -= 1

    return min_mp

def main():
    N, A, B, C = map(int, input().split())
    lengths = list(map(int, input().split()))
    print(get_min_mp(N, A, B, C, lengths))

if __name__ == '__main__':
    main()

