
def count_good_arrays(n, k, a):
    # Initialize a count of good arrays to 0
    count = 0
    
    # Iterate over each element in the array
    for i in range(n):
        # If the current element is -1, we can replace it with any integer from 1 to k
        if a[i] == -1:
            # Increment the count by the number of good arrays we can obtain by replacing the current element with each integer from 1 to k
            count += (k - 1)
        # If the current element is not -1, we can only replace it with the current element
        else:
            # Increment the count by 1
            count += 1
    
    # Return the count modulo 998244353
    return count % 998244353

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(count_good_arrays(n, k, a))

