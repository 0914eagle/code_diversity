
def f1(n, m, similar_pairs):
    # Initialize the division arrays
    division_1 = []
    division_2 = []

    # Loop through each similar pair
    for pair in similar_pairs:
        # If the problem is not already in a division, add it to division 1
        if pair[0] not in division_1 and pair[0] not in division_2:
            division_1.append(pair[0])
        # If the problem is not already in a division, add it to division 2
        if pair[1] not in division_1 and pair[1] not in division_2:
            division_2.append(pair[1])

    # Return the number of ways to split the problems
    return len(division_1) * len(division_2)

def f2(n, m, similar_pairs):
    # Initialize the division arrays
    division_1 = []
    division_2 = []

    # Loop through each similar pair
    for pair in similar_pairs:
        # If the problem is not already in a division, add it to division 1
        if pair[0] not in division_1 and pair[0] not in division_2:
            division_1.append(pair[0])
        # If the problem is not already in a division, add it to division 2
        if pair[1] not in division_1 and pair[1] not in division_2:
            division_2.append(pair[1])

    # Return the number of ways to split the problems
    return len(division_1) * len(division_2)

if __name__ == '__main__':
    n, m = map(int, input().split())
    similar_pairs = []
    for _ in range(m):
        similar_pairs.append(list(map(int, input().split())))
    print(f1(n, m, similar_pairs))
    print(f2(n, m, similar_pairs))

