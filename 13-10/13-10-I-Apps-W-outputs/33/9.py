
def get_pairs(numbers):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            pairs.append(numbers[i] * numbers[j])
    return pairs

def get_kth_smallest(pairs, k):
    return sorted(pairs)[k-1]

def main():
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    pairs = get_pairs(numbers)
    print(get_kth_smallest(pairs, k))

if __name__ == '__main__':
    main()

