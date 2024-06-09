
def solve(arr):
    n = len(arr)
    k = len(bin(max(arr))[2:])
    xor_sum = 0
    for i in range(n):
        xor_sum ^= arr[i]
    segments = [i for i in range(1, n + 1) if xor_sum ^ arr[i - 1] ^ arr[i] != 0]
    return len(segments)

