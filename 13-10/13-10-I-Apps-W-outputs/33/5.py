
def get_pairs(numbers):
    n = len(numbers)
    pairs = []
    for i in range(n-1):
        for j in range(i+1, n):
            pairs.append(numbers[i] * numbers[j])
    return pairs

def get_kth_pair(numbers, k):
    pairs = get_pairs(numbers)
    pairs.sort()
    return pairs[k-1]

def main():
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(get_kth_pair(numbers, k))

if __name__ == '__main__':
    main()

