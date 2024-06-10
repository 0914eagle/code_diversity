
def count_valid_pairs(n, k):
    toys = {}
    count = 0
    for i in range(1, n + 1):
        toys[i] = True

    for i in range(1, n + 1):
        if k - i in toys and k - i != i:
            count += 1

    return count

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(count_valid_pairs(n, k))
