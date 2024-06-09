
def count_arrays(n, m):
    # Initialize a list to store the arrays
    arrays = []
    
    # Iterate over all possible arrays
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            for k in range(1, m + 1):
                # Check if the array satisfies the conditions
                if i != j and j != k and k != i and i < j and j < k:
                    arrays.append([i, j, k])
    
    # Return the number of arrays modulo 998244353
    return len(arrays) % 998244353

def main():
    # Read the input n and m
    n, m = map(int, input().split())
    
    # Call the count_arrays function and print the result
    print(count_arrays(n, m))

if __name__ == '__main__':
    main()

