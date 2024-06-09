
def get_min_mp(bamboos, A, B, C):
    # Initialize the minimum MP needed to achieve the objective
    min_mp = 0

    # Sort the bamboos in non-decreasing order
    bamboos.sort()

    # Use Extension Magic to increase the length of the shortest bamboo to A
    while bamboos[0] < A:
        min_mp += 1
        bamboos[0] += 1

    # Use Composition Magic to combine the two longest bamboos to obtain a bamboo of length B
    while len(bamboos) > 2 and bamboos[-1] + bamboos[-2] > B:
        min_mp += 10
        bamboos[-2:] = [bamboos[-1] + bamboos[-2]]

    # Use Shortening Magic to decrease the length of the longest bamboo to C
    while bamboos[-1] > C:
        min_mp += 1
        bamboos[-1] -= 1

    return min_mp

def main():
    N, A, B, C = map(int, input().split())
    bamboos = list(map(int, input().split()))
    print(get_min_mp(bamboos, A, B, C))

if __name__ == '__main__':
    main()

