
def find_smallest_subsegment(n, arr):
    freq = {}
    max_freq = 0
    left, right = 0, 0
    smallest_subsegment = (0, n - 1)

    while right < n:
        if arr[right] not in freq:
            freq[arr[right]] = 0
        freq[arr[right]] += 1
        max_freq = max(max_freq, freq[arr[right]])

        while right - left + 1 - max_freq > 0:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]
            left += 1

        if right - left < smallest_subsegment[1] - smallest_subsegment[0]:
            smallest_subsegment = (left, right)

        right += 1

    return smallest_subsegment

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    result = find_smallest_subsegment(n, arr)
    print(result[0] + 1, result[1] + 1)
