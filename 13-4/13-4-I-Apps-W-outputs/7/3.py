
def f1(n, m, similar_pairs):
    # Initialize the division arrays
    division1 = [False] * (n + 1)
    division2 = [False] * (n + 1)

    # Mark the problems as similar
    for pair in similar_pairs:
        division1[pair[0]] = True
        division2[pair[1]] = True

    # Count the number of ways to split the problems
    count = 0
    for i in range(1, n + 1):
        if division1[i] and division2[i]:
            count += 1

    return count

def f2(n, m, similar_pairs):
    # Initialize the division arrays
    division1 = [False] * (n + 1)
    division2 = [False] * (n + 1)

    # Mark the problems as similar
    for pair in similar_pairs:
        division1[pair[0]] = True
        division2[pair[1]] = True

    # Count the number of ways to split the problems
    count = 0
    for i in range(1, n + 1):
        if division1[i] and division2[i]:
            count += 1

    return count

if __name__ == '__main__':
    n, m = map(int, input().split())
    similar_pairs = []
    for _ in range(m):
        similar_pairs.append(list(map(int, input().split())))

    count = f1(n, m, similar_pairs)
    print(count)

