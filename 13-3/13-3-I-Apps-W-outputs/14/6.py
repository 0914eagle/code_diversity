
def count_good_arrays(n, k, a):
    # Initialize the number of good arrays to 0
    num_good_arrays = 0
    
    # Iterate over each element in the array
    for i in range(n):
        # If the current element is -1, we can replace it with any integer from 1 to k
        if a[i] == -1:
            # Increment the number of good arrays by the number of ways to replace -1 with an integer from 1 to k
            num_good_arrays += k
        # If the current element is not -1, we can only replace it with the current element
        else:
            # Increment the number of good arrays by 1
            num_good_arrays += 1
    
    # Return the number of good arrays modulo 998244353
    return num_good_arrays % 998244353

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(count_good_arrays(n, k, a))

