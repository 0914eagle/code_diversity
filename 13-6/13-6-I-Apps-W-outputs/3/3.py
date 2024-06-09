
def count_asc_desc_arrays(n, m):
    # Initialize a list to store the arrays
    arrays = []
    
    # Loop through all possible arrays
    for i in range(1, m + 1):
        for j in range(i + 1, m + 1):
            for k in range(j + 1, m + 1):
                # Check if the array has exactly one pair of equal elements
                if i == j or j == k or k == i:
                    continue
                # Check if the array is strictly ascending before the i-th element and strictly descending after it
                if i < j and j < k and k > i:
                    arrays.append([i, j, k])
    
    # Return the number of arrays modulo 998244353
    return len(arrays) % 998244353

def main():
    n, m = map(int, input().split())
    print(count_asc_desc_arrays(n, m))

if __name__ == '__main__':
    main()

