
def get_subsequence_beauty(subsequence, n):
    beauty = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            beauty += abs(subsequence[i] - subsequence[j])
    return beauty

def get_sum_of_beauty(arr, k):
    n = len(arr)
    beauty_sum = 0
    for i in range(n - k + 1):
        subsequence = arr[i:i+k]
        beauty_sum += get_subsequence_beauty(subsequence, k)
    return beauty_sum % 998244353

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_sum_of_beauty(arr, k))

if __name__ == '__main__':
    main()

