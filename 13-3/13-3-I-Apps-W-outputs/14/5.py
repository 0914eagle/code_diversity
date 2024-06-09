
def count_good_arrays(n, k, a):
    # Initialize a count of good arrays to 0
    count = 0
    
    # Iterate over each element in the array
    for i in range(n):
        # If the current element is -1, increment the count by the number of good arrays that can be obtained by replacing it with each of the numbers from 1 to k
        if a[i] == -1:
            count += (k ** (n - i - 1))
        # If the current element is not -1, decrement the count by the number of good arrays that contain a bad subarray starting at the current element and ending at the end of the array
        else:
            count -= (k ** (n - i - 1))
    
    # Return the count modulo 998244353
    return count % 998244353

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(count_good_arrays(n, k, a))

