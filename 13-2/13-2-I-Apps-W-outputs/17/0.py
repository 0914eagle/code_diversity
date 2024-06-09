
def solve(a, queries):
    # Initialize an empty list to store the results
    results = []
    
    # Loop through each query
    for query in queries:
        # Reverse the segment of the permutation specified by the query
        a = a[:query[0]] + a[query[0]:query[1]+1][::-1] + a[query[1]+1:]
        
        # Count the number of inversions in the permutation
        inversions = 0
        for i in range(len(a)-1):
            for j in range(i+1, len(a)):
                if a[i] > a[j]:
                    inversions += 1
        
        # Add the result to the list of results
        results.append("odd" if inversions % 2 == 1 else "even")
    
    # Return the list of results
    return results

