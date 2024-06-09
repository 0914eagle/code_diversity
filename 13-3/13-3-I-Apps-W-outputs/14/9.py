
def count_good_arrays(n, k, a):
    # Initialize a dictionary to count the number of good arrays
    good_arrays = {}
    
    # Iterate over each element in the array
    for i in range(n):
        # If the current element is -1, we can replace it with any integer from 1 to k
        if a[i] == -1:
            # Iterate over each possible replacement
            for j in range(1, k+1):
                # If the current replacement is valid, i.e., it does not create a bad subarray, we can add it to the dictionary
                if is_valid_replacement(i, j, a):
                    good_arrays[j] = good_arrays.get(j, 0) + 1
    
    # Return the sum of all good arrays
    return sum(good_arrays.values()) % 998244353

def is_valid_replacement(i, j, a):
    # If the current element is -1 and the replacement is valid, we can add it to the dictionary
    if a[i] == -1 and j not in a[0:i] and j not in a[i+1:]:
        return True
    return False

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(count_good_arrays(n, k, a))

