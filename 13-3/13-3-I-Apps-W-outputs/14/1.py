
def count_good_arrays(n, k, a):
    # Initialize a dictionary to count the number of good arrays
    good_arrays = {}
    
    # Iterate over each element in the array
    for i in range(n):
        # If the current element is -1, we can replace it with any integer from 1 to k
        if a[i] == -1:
            # Iterate over each possible replacement
            for j in range(1, k+1):
                # If the current replacement is valid, i.e., it does not create a bad subarray, increment the count
                if is_valid_replacement(i, j, a):
                    good_arrays[j] = good_arrays.get(j, 0) + 1
        # If the current element is not -1, we can only replace it with itself
        else:
            good_arrays[a[i]] = good_arrays.get(a[i], 0) + 1
    
    # Return the sum of the counts modulo 998244353
    return sum(good_arrays.values()) % 998244353

def is_valid_replacement(i, j, a):
    # If the current element is the first element of a bad subarray, return False
    if i > 0 and a[i-1] == j and a[i] == j:
        return False
    # If the current element is the last element of a bad subarray, return False
    if i < len(a)-1 and a[i+1] == j and a[i] == j:
        return False
    # Otherwise, return True
    return True

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(count_good_arrays(n, k, a))

