
def f1(n, m, similar_pairs):
    # Initialize the division arrays
    division1 = []
    division2 = []

    # Iterate over the similar pairs
    for pair in similar_pairs:
        # If the problem is not already in a division, add it to the other division
        if pair[0] not in division1 and pair[0] not in division2:
            division2.append(pair[0])
        elif pair[1] not in division1 and pair[1] not in division2:
            division2.append(pair[1])
        # If the problem is already in a division, add the other problem to the other division
        elif pair[0] in division1 and pair[1] not in division1 and pair[1] not in division2:
            division2.append(pair[1])
        elif pair[1] in division1 and pair[0] not in division1 and pair[0] not in division2:
            division2.append(pair[0])
        # If both problems are already in divisions, find the harder problem and add it to the other division
        elif pair[0] in division1 and pair[1] in division1:
            if pair[0] > pair[1]:
                division2.append(pair[1])
            else:
                division2.append(pair[0])
        elif pair[0] in division2 and pair[1] in division2:
            if pair[0] > pair[1]:
                division1.append(pair[1])
            else:
                division1.append(pair[0])

    # Return the number of ways to split the problems
    return len(division1) * len(division2)

def f2(...):
    # Implement the second function here
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    similar_pairs = []
    for _ in range(m):
        similar_pairs.append(list(map(int, input().split())))
    print(f1(n, m, similar_pairs))

