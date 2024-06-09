
def get_maximum_segments(arr, k):
    # Replace each element with its complement
    arr = [2**k - 1 - x for x in arr]
    # XOR all elements together
    result = arr[0]
    for i in range(1, len(arr)):
        result ^= arr[i]
    return bin(result).count("1")

