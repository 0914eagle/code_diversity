_smallest_subsegment(n, arr):
    freq = {}
    max_freq = 0
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        max_freq = max(max_freq, freq[num])
    
    left, right = 0, 0
    min_length = float('inf')
    min_left, min_right = 0, n - 1
    
    while right < n:
        while right < n and freq[arr[right]] < max_freq:
            freq[arr[right]] += 1
            right += 1
        
        if right == n:
            break
        
        while left < right and freq[arr[left]] > max_freq:
            freq[arr[left]] -= 1
            left += 1
        
        if right - left < min_length:
            min_length = right - left
            min_left, min_right = left, right
        
        right += 1
    
    return min_left + 1, min_right + 1

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    l, r = find_smallest_subsegment(n, arr)
    print(l, r