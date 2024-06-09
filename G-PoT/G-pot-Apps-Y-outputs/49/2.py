
n = int(input())
a = list(map(int, input().split()))

def find_max_length(n, a):
    def is_increasing(arr):
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i+1]:
                return False
        return True

    max_length = 1
    for i in range(n):
        if i > 0 and i < n - 1 and a[i-1] < a[i+1]:
            max_length = max(max_length, i + 1)
        elif is_increasing(a[:i] + a[i+1:]):
            max_length = max(max_length, i)

    return max_length

print(find_max_length(n, a))
