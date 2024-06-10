
def find_smallest_subsegment(n, arr):
    freq = {}
    left, right = 0, 0
    max_freq = 0
    min_len = n
    start, end = 0, n - 1

    while right < n:
        freq[arr[right]] = freq.get(arr[right], 0) + 1
        max_freq = max(max_freq, freq[arr[right]])

        while right - left + 1 - max_freq > 0:
            freq[arr[left]] -= 1
            left += 1

        if right - left + 1 == max_freq and right - left < min_len:
            min_len = right - left
            start, end = left, right

        right += 1

    return start + 1, end + 1

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    l, r = find_smallest_subsegment(n, arr)
    print(l, r)
