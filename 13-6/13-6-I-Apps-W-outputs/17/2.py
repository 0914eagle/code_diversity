
def solve(arr):
    n = len(arr)
    k = len(bin(max(arr))[2:])
    xor_sum = 0
    for i in range(n):
        xor_sum ^= arr[i]
    result = xor_sum
    for i in range(n):
        xor_sum ^= arr[i]
        result = max(result, xor_sum)
        xor_sum ^= arr[i]
    return result

