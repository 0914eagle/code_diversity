
def get_min_mp(N, A, B, C, lengths):
    # Initialize the minimum MP needed to achieve the objective
    min_mp = 0

    # Initialize the list of available bamboos
    available_bamboos = lengths[:]

    # Sort the available bamboos in descending order
    available_bamboos.sort(reverse=True)

    # Use Extension Magic to increase the length of the first bamboo to A
    if available_bamboos[0] < A:
        min_mp += A - available_bamboos[0]
        available_bamboos[0] = A

    # Use Composition Magic to combine the first two bamboos to obtain a bamboo of length B
    if available_bamboos[0] + available_bamboos[1] < B:
        min_mp += B - (available_bamboos[0] + available_bamboos[1])
        available_bamboos[0] = B
        available_bamboos.pop(1)

    # Use Shortening Magic to decrease the length of the first bamboo to C
    if available_bamboos[0] > C:
        min_mp += available_bamboos[0] - C
        available_bamboos[0] = C

    # Return the minimum MP needed to achieve the objective
    return min_mp

def main():
    N, A, B, C = map(int, input().split())
    lengths = list(map(int, input().split()))
    print(get_min_mp(N, A, B, C, lengths))

if __name__ == '__main__':
    main()

