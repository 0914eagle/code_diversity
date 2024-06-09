
def get_min_mp(n, a, b, c, lengths):
    # Initialize the minimum MP needed to achieve the objective
    min_mp = 0

    # Initialize the list of bamboos
    bamboos = lengths[:]

    # Sort the bamboos in descending order
    bamboos.sort(reverse=True)

    # Use Extension Magic to increase the length of the shortest bamboo to A
    while bamboos[0] < a:
        min_mp += 1
        bamboos[0] += 1

    # Use Composition Magic to combine the two shortest bamboos to obtain a bamboo of length B
    while len(bamboos) > 2 and bamboos[1] + bamboos[2] == b:
        min_mp += 10
        bamboos[1] += bamboos[2]
        del bamboos[2]

    # Use Shortening Magic to decrease the length of the longest bamboo to C
    while bamboos[0] > c:
        min_mp += 1
        bamboos[0] -= 1

    return min_mp

def main():
    n, a, b, c = map(int, input().split())
    lengths = list(map(int, input().split()))
    print(get_min_mp(n, a, b, c, lengths))

if __name__ == '__main__':
    main()

