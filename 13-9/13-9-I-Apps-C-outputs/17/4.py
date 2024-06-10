
def get_contiguous_subsequence(arr, k):
    return sorted(arr[:k])

def get_smallest_element(arr, k):
    return min(get_contiguous_subsequence(arr, k))

def get_largest_element(arr, k):
    return max(get_contiguous_subsequence(arr, k))

def get_smallest_difference(arr, k, q):
    smallest_difference = float('inf')
    for i in range(q):
        smallest_element = get_smallest_element(arr, k)
        largest_element = get_largest_element(arr, k)
        difference = largest_element - smallest_element
        if difference < smallest_difference:
            smallest_difference = difference
        arr = arr[1:]
    return smallest_difference

if __name__ == '__main__':
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_smallest_difference(arr, k, q))

