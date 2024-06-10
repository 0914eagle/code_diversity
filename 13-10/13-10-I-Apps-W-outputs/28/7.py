
def get_minimum_days(n, k, pebbles):
    # Count the number of pebbles of each type
    counts = [0] * (n + 1)
    for i in range(n):
        counts[i] = pebbles[i]

    # Sort the pebbles by type
    sorted_pebbles = sorted(pebbles)

    # Initialize the minimum number of days to collect all pebbles
    min_days = 0

    # Loop through the pebbles and count the number of days needed to collect all pebbles
    for i in range(n):
        min_days += (counts[i] - 1) // k + 1

    return min_days

def main():
    n, k = map(int, input().split())
    pebbles = list(map(int, input().split()))
    print(get_minimum_days(n, k, pebbles))

if __name__ == '__main__':
    main()

