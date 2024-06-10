
def count_valid_pairs(n, k):
    toy_costs = {}
    valid_pairs = 0

    for i in range(1, n + 1):
        toy_costs[i] = True

    for i in range(1, n + 1):
        if k - i in toy_costs and k - i != i:
            valid_pairs += 1

    return valid_pairs

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(count_valid_pairs(n, k))
