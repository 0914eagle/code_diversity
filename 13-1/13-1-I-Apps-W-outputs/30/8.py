
def get_dominated_subarray(arr):
    # Step 1: Find the most frequent element in the array
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    most_freq = max(freq, key=freq.get)

    # Step 2: Find the shortest subarray that contains the most frequent element
    min_len = len(arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == most_freq and arr[j] == most_freq:
                min_len = min(min_len, j-i+1)

    return min_len if min_len < len(arr) else -1

def main():
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        arr = list(map(int, input().split()))
        print(get_dominated_subarray(arr))

if __name__ == '__main__':
    main()

