
def f1(N, Q):
    # Initialize the array of stones
    stones = [0] * (N + 1)
    
    # Loop through each query
    for _ in range(Q):
        # Read the query type and values
        query_type, u, v = map(int, input().split())
        
        # If the query is to put a stone inside a box
        if query_type == 1:
            # Put a stone inside the box with equal probability
            stones[u] += 1
            stones[v] += 1
        
        # If the query is to calculate the expected value
        elif query_type == 2:
            # Calculate the expected value of the sum of squares of the stones
            expected_value = sum([stones[i] ** 2 for i in range(1, N + 1)])
            
            # Print the result
            print(expected_value)
            
def f2(...):
    # Function 2 code
    ...
    
if __name__ == '__main__':
    N, Q = map(int, input().split())
    f1(N, Q)

