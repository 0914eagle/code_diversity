
def get_maximum_sum(a, edges):
    # Initialize the maximum sum and the set of gifts that hang on the first gift
    max_sum = 0
    gifts = set([1])

    # Iterate over the edges and update the maximum sum and the set of gifts that hang on the first gift
    for u, v in edges:
        if u in gifts:
            gifts.add(v)
            max_sum += a[v - 1]
        elif v in gifts:
            gifts.add(u)
            max_sum += a[u - 1]

    # Return the maximum sum
    return max_sum

def get_chloe_and_vladik_sum(a, edges):
    # Initialize the maximum sum and the set of gifts that hang on the first gift
    max_sum = 0
    gifts = set([1])

    # Iterate over the edges and update the maximum sum and the set of gifts that hang on the first gift
    for u, v in edges:
        if u in gifts and v in gifts:
            continue
        if u in gifts:
            gifts.add(v)
            max_sum += a[v - 1]
        elif v in gifts:
            gifts.add(u)
            max_sum += a[u - 1]

    # Return the maximum sum
    return max_sum

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))

    # Get the maximum sum
    max_sum = get_maximum_sum(a, edges)

    # Get the sum for Chloe and Vladik
    chloe_and_vladik_sum = get_chloe_and_vladik_sum(a, edges)

    # Print the result
    if chloe_and_vladik_sum == max_sum:
        print(chloe_and_vladik_sum)
    else:
        print("Impossible")

if __name__ == '__main__':
    main()

