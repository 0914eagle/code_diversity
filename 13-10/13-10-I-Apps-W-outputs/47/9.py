
def get_beauty(arr, k):
    # Calculate the beauty of the array
    beauty = 0
    for i in range(len(arr) - k + 1):
        for j in range(i + 1, len(arr)):
            beauty += abs(arr[i] - arr[j])
    return beauty

def get_subsequence_beauty(arr, k):
    # Calculate the beauty of all subsequences of the array of length k
    beauty = 0
    for i in range(len(arr) - k + 1):
        subarr = arr[i:i+k]
        beauty += get_beauty(subarr, k)
    return beauty

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_subsequence_beauty(arr, k) % 998244353)

if __name__ == '__main__':
    main()

