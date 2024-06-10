
def find_smallest_subsegment(n, arr):
    freq = {}
    left, right = 0, 0
    max_freq = 0
    smallest_subsegment = (0, n - 1)

    while right < n:
        freq[arr[right]] = freq.get(arr[right], 0) + 1
        max_freq = max(max_freq, freq[arr[right]])

        while right - left + 1 - max_freq > 0:
            freq[arr[left]] -= 1
            left += 1

        if right - left < smallest_subsegment[1] - smallest_subsegment[0]:
            smallest_subsegment = (left, right)

        right += 1

    return smallest_subsegment

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    l, r = find_smallest_subsegment(n, arr)
    print(l + 1, r + 1)
