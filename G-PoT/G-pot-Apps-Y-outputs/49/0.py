
n = int(input())
a = list(map(int, input().split()))

def find_max_length(a):
    def is_increasing(arr):
        for i in range(len(arr) - 1):
            if arr[i] >= arr[i + 1]:
                return False
        return True

    max_length = 1
    for i in range(n):
        if i == 0:
            max_length = max(max_length, 1 + is_increasing(a[i+1:]))
        elif i == n - 1:
            max_length = max(max_length, 1 + is_increasing(a[:i]))
        else:
            if a[i-1] < a[i+1]:
                max_length = max(max_length, 2 + is_increasing(a[:i] + a[i+1:]))
            else:
                max_length = max(max_length, 1 + is_increasing(a[:i]))

    return max_length

print(find_max_length(a))
