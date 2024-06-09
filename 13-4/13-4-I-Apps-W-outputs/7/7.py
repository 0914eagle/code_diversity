
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
    for i in range(1 << n):
        # Initialize the count of problems in division 1
        count_div1 = 0

        # Iterate over all problems
        for j in range(1, n + 1):
            # If the problem is in division 1, increment the count
            if i & (1 << (j - 1)):
                count_div1 += 1

        # If the count of problems in division 1 is non-zero, check if the division satisfies all the rules
        if count_div1 > 0:
            # Initialize the count of problems in division 2
            count_div2 = n - count_div1

            # Iterate over all problems in division 1
            for j in range(1, n + 1):
                # If the problem is in division 1, check if it is harder than any problem in division 2
                if i & (1 << (j - 1)):
                    for k in range(1, n + 1):
                        # If the problem is in division 2 and is similar to the current problem, increment the count
                        if not (i & (1 << (k - 1))) and k in graph[j]:
                            count_div2 += 1

            # If the count of problems in division 2 is non-zero and the division satisfies all the rules, increment the count of ways
            if count_div2 > 0 and count_div1 > count_div2:
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

