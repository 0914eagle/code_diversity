
import sys

def get_gis_permutations(g, n):
    # Initialize the permutation with the first element of g
    permutation = [g[0]]
    
    # Iterate over the remaining elements of g
    for i in range(1, len(g)):
        # Find the leftmost element in the permutation that is greater than the current element of g
        index = next((j for j in range(i, n) if permutation[j] > g[i]), None)
        
        # If such an element exists, insert it into the permutation
        if index is not None:
            permutation.insert(index, g[i])
        # Otherwise, the permutation is not possible, so return 0
        else:
            return 0
    
    # The permutation is possible, so return the number of ways to permute the elements
    return math.factorial(n) // math.factorial(n - len(g))

def main():
    n, l = map(int, input().split())
    g = list(map(int, input().split()))
    print(get_gis_permutations(g, n))

if __name__ == "__main__":
    main()

