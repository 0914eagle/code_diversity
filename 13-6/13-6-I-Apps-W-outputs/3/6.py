
def count_arrays(n, m):
    # Initialize a list to store the results
    results = []
    
    # Iterate over all possible values of the first element
    for i in range(1, m + 1):
        # Add the first element to the list
        results.append(i)
        # Iterate over the remaining elements
        for j in range(1, n - 1):
            # Add the next element, which must be different from the previous element
            results.append(j + 1)
        # Add the last element, which must be different from all the previous elements
        results.append(1)
    
    # Return the number of arrays that meet the conditions, taken modulo 998244353
    return len(results) % 998244353

def main():
    # Read the input data
    n, m = map(int, input().split())
    
    # Call the count_arrays function and print the result
    print(count_arrays(n, m))

if __name__ == '__main__':
    main()

