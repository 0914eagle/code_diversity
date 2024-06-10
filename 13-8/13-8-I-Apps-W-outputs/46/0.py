
def get_pairs(n, k):
    # find all pairs of numbers that satisfy the condition
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if a[i] * a[j] == k:
                pairs.append((i, j))
    return pairs

def count_pairs(n, k):
    # count the number of pairs
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] * a[j] == k:
                count += 1
    return count

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    pairs = get_pairs(n, k)
    count = count_pairs(n, k)
    print(count)

if __name__ == '__main__':
    main()

