
def get_pairs(numbers):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            pairs.append(numbers[i] * numbers[j])
    return pairs

def get_kth_pair(numbers, k):
    pairs = get_pairs(numbers)
    pairs.sort()
    return pairs[k-1]

def main():
    numbers = list(map(int, input().split()))
    k = int(input())
    print(get_kth_pair(numbers, k))

if __name__ == '__main__':
    main()

