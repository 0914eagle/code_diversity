
def f1(N, Q):
    # Initialize the number of stones in each box to 0
    stones = [0] * (N + 1)
    
    # Loop through each query
    for _ in range(Q):
        # Read the query type and values
        query_type, u, v = map(int, input().split())
        
        # If the query type is 1, put a stone inside one of the boxes between u and v
        if query_type == 1:
            # Choose a random box between u and v
            box = random.randint(u, v)
            
            # Increment the number of stones in the chosen box
            stones[box] += 1
        
        # If the query type is 2, calculate the expected value of A
        elif query_type == 2:
            # Calculate the sum of the squares of the number of stones in each box
            sum_squares = sum([stone ** 2 for stone in stones])
            
            # Return the expected value of A
            return sum_squares
    
    # If all queries have been processed, return the number of stones in the last box
    return stones[-1]

def f2(N, Q):
    # Initialize the number of stones in each box to 0
    stones = [0] * (N + 1)
    
    # Loop through each query
    for _ in range(Q):
        # Read the query type and values
        query_type, u, v = map(int, input().split())
        
        # If the query type is 1, put a stone inside one of the boxes between u and v
        if query_type == 1:
            # Choose a random box between u and v
            box = random.randint(u, v)
            
            # Increment the number of stones in the chosen box
            stones[box] += 1
        
        # If the query type is 2, calculate the expected value of A
        elif query_type == 2:
            # Calculate the sum of the squares of the number of stones in each box
            sum_squares = sum([stone ** 2 for stone in stones])
            
            # Return the expected value of A
            return sum_squares
    
    # If all queries have been processed, return the number of stones in the last box
    return stones[-1]

if __name__ == '__main__':
    N, Q = map(int, input().split())
    print(f1(N, Q))
    print(f2(N, Q))

