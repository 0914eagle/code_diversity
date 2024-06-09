
def solve(a, queries):
    # Initialize an empty list to store the results
    results = []
    
    # Loop through each query
    for l, r in queries:
        # Reverse the segment [l, r] of the permutation
        a[l:r+1] = a[l:r+1][::-1]
        
        # Count the number of inversions in the permutation
        count = 0
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                if a[i] > a[j]:
                    count += 1
        
        # Add the result to the list
        results.append("odd" if count % 2 == 1 else "even")
    
    return results

