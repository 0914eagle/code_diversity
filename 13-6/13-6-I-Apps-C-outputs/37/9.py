
def f1(N, Q):
    # Initialize the array of stones
    stones = [0] * (N + 1)
    
    # Iterate over the queries
    for _ in range(Q):
        # Read the query type and values
        query_type, u, v = map(int, input().split())
        
        # If the query is to put a stone inside a box
        if query_type == 1:
            # Put a stone inside the box with equal probability
            stones[u] += 1
            stones[v] += 1
        
        # If the query is to calculate the expected value of A
        elif query_type == 2:
            # Calculate the expected value of A
            expected_A = 0
            for i in range(1, N + 1):
                expected_A += stones[i] ** 2
            
            # Print the expected value of A modulo 10^9 + 7
            print(expected_A % (10**9 + 7))

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    N, Q = map(int, input().split())
    f1(N, Q)

