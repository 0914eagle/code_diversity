
def count_ways(n, m, similar_pairs):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges between similar problems
    for u, v in similar_pairs:
        graph[u].append(v)
        graph[v].append(u)

    # Initialize the count of ways to split problems
    ways = 0

    # Iterate over all possible divisions
    for i in range(1, n + 1):
        # Initialize the division 1 with problem i
        division_1 = [i]

        # Initialize the division 2 as an empty set
        division_2 = set()

        # Iterate over all problems in division 1
        for j in division_1:
            # Add all problems that are similar to j to division 2
            for k in graph[j]:
                if k not in division_2:
                    division_2.add(k)

        # Check if division 2 is non-empty
        if len(division_2) == 0:
            continue

        # Check if all problems are used in exactly one division
        if len(division_1 | division_2) != n:
            continue

        # Check if all problems in division 1 are harder than any problem in division 2
        if any(division_1[j] <= division_2[k] for j in range(len(division_1)) for k in range(len(division_2))):
            continue

        # Increment the count of ways to split problems
        ways += 1

    return ways

def main():
    n, m = map(int, input().split())
    similar_pairs = []
    for _ in range(m):
        u, v = map(int, input().split())
        similar_pairs.append((u, v))
    print(count_ways(n, m, similar_pairs))

if __name__ == '__main__':
    main()

