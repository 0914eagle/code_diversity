
def get_min_mp(N, A, B, C, lengths):
    # Initialize the minimum MP needed to achieve the objective
    min_mp = 0

    # Initialize the number of bamboos needed to achieve the objective
    num_bamboos_needed = 3

    # Initialize the dictionary to store the bamboos and their lengths
    bamboos = {}

    # Add the input bamboos to the dictionary
    for i in range(N):
        bamboos[i] = lengths[i]

    # While there are still bamboos needed to achieve the objective
    while num_bamboos_needed > 0:
        # Find the longest bamboo that is not yet used
        longest_bamboo = -1
        for i in range(N):
            if bamboos[i] > 0 and (longest_bamboo == -1 or bamboos[i] > bamboos[longest_bamboo]):
                longest_bamboo = i

        # If there is no longer bamboo, break the loop
        if longest_bamboo == -1:
            break

        # Use the Extension Magic to increase the length of the longest bamboo by 1
        bamboos[longest_bamboo] += 1
        min_mp += 1
        num_bamboos_needed -= 1

    # While there are still bamboos needed to achieve the objective
    while num_bamboos_needed > 0:
        # Find the longest bamboo that is not yet used
        longest_bamboo = -1
        for i in range(N):
            if bamboos[i] > 0 and (longest_bamboo == -1 or bamboos[i] > bamboos[longest_bamboo]):
                longest_bamboo = i

        # If there is no longer bamboo, break the loop
        if longest_bamboo == -1:
            break

        # Use the Shortening Magic to decrease the length of the longest bamboo by 1
        bamboos[longest_bamboo] -= 1
        min_mp += 1
        num_bamboos_needed -= 1

    # While there are still bamboos needed to achieve the objective
    while num_bamboos_needed > 0:
        # Find the two longest bamboos that are not yet used
        longest_bamboo1 = -1
        longest_bamboo2 = -1
        for i in range(N):
            if bamboos[i] > 0 and (longest_bamboo1 == -1 or bamboos[i] > bamboos[longest_bamboo1]):
                longest_bamboo1 = i
                longest_bamboo2 = -1
            elif bamboos[i] > 0 and (longest_bamboo2 == -1 or bamboos[i] > bamboos[longest_bamboo2]):
                longest_bamboo2 = i

        # If there is no longer bamboo, break the loop
        if longest_bamboo1 == -1 or longest_bamboo2 == -1:
            break

        # Use the Composition Magic to combine the two longest bamboos
        bamboos[longest_bamboo1] += bamboos[longest_bamboo2]
        bamboos[longest_bamboo2] = 0
        min_mp += 10
        num_bamboos_needed -= 1

    return min_mp

def main():
    N, A, B, C = map(int, input().split())
    lengths = list(map(int, input().split()))
    print(get_min_mp(N, A, B, C, lengths))

if __name__ == '__main__':
    main()

