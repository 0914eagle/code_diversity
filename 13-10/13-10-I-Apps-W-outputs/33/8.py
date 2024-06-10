
def get_pairs(numbers):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            pairs.append(numbers[i] * numbers[j])
    return pairs

def get_sorted_pairs(numbers):
    return sorted(get_pairs(numbers))

def get_kth_pair(numbers, k):
    pairs = get_sorted_pairs(numbers)
    return pairs[k-1]

def main():
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(get_kth_pair(numbers, k))

if __name__ == '__main__':
    main()

