
def count_ways_to_make_figure_complete(N, d):
    # Initialize the answer to 0
    answer = 0
    
    # Base case: if N is 1, there is only one way to make the figure complete
    if N == 1:
        return 1
    
    # Recursive case: consider all possible connections between parts
    for i in range(N):
        for j in range(i+1, N):
            # If parts i and j have at least one common hole, we can connect them
            if d[i] > 0 and d[j] > 0:
                # Recursively count the number of ways to make the figure complete with parts i and j connected
                answer += count_ways_to_make_figure_complete(N-1, d[:i] + d[i]-1 + d[i+1:] + d[j]-1 + d[j+1:])
    
    # Return the answer modulo 998244353
    return answer % 998244353

