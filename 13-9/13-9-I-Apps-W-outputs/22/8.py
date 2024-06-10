
def xor(a, b):
    return a ^ b

def get_xor_of_subarray(arr, l, r):
    result = arr[l]
    for i in range(l + 1, r + 1):
        result = xor(result, arr[i])
    return result

def count_pairs_with_equal_sum_and_xor(arr):
    n = len(arr)
    count = 0
    for l in range(n):
        for r in range(l, n):
            if get_xor_of_subarray(arr, l, r) == sum(arr[l:r + 1]):
                count += 1
    return count

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_pairs_with_equal_sum_and_xor(arr))

if __name__ == '__main__':
    main()

