
def find_smallest_subsegment(n, arr):
    freq = {}
    max_freq = 0
    left, right = 0, 0
    smallest_length = float('inf')
    result = (0, 0)

    while right < n:
        freq[arr[right]] = freq.get(arr[right], 0) + 1
        max_freq = max(max_freq, freq[arr[right]])

        while right - left + 1 - max_freq > 0:
            freq[arr[left]] -= 1
            left += 1

        if right - left + 1 < smallest_length:
            smallest_length = right - left + 1
            result = (left, right)

        right += 1

    return result

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    l, r = find_smallest_subsegment(n, arr)
    print(l + 1, r + 1)
