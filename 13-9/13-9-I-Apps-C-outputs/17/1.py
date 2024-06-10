
def get_optimal_subsequence(arr, k):
    # Sort the array in ascending order
    arr.sort()
    # Initialize the smallest and largest elements removed as the first and last elements of the array
    smallest, largest = arr[0], arr[-1]
    # Iterate over the array and remove the smallest element in each contiguous subsequence of length k
    for i in range(len(arr) - k + 1):
        smallest = min(smallest, arr[i + k - 1])
        largest = max(largest, arr[i])
    # Return the difference between the largest and smallest elements removed
    return largest - smallest

def main():
    # Read the input data from stdin
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    # Find the smallest possible value of X-Y by calling the get_optimal_subsequence function
    print(get_optimal_subsequence(arr, k))

if __name__ == '__main__':
    main()

