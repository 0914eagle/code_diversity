
n = int(input())
a = list(map(int, input().split()))

def max_increasing_subarray(a):
    def increasing_length(arr):
        length = 1
        max_length = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                length += 1
                max_length = max(max_length, length)
            else:
                length = 1
        return max_length

    max_len = 1
    for i in range(1, len(a)-1):
        if a[i-1] < a[i+1]:
            max_len = max(max_len, increasing_length(a[i-1:i+2]))
    
    return max_len

result = max_increasing_subarray(a)
print(result)
