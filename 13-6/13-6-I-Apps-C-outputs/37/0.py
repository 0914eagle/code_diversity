
def f1(n, q):
    # Initialize the number of stones in each box to 0
    num_stones = [0] * (n + 1)
    # Initialize the probability of each box to 1
    prob = [1] * (n + 1)
    
    # Loop through each query
    for _ in range(q):
        # Read the query type and the indices of the boxes
        query_type, u, v = map(int, input().split())
        
        # If the query type is 1, put a stone in one of the boxes between u and v
        if query_type == 1:
            # Loop through each box between u and v
            for i in range(u, v + 1):
                # Add the probability of the box to the probability of the previous box
                prob[i] += prob[i - 1]
                # Add the number of stones in the box to the number of stones in the previous box
                num_stones[i] += num_stones[i - 1]
        # If the query type is 2, calculate the expected value of the number of stones in all boxes
        else:
            # Initialize the expected value to 0
            expected_value = 0
            # Loop through each box
            for i in range(1, n + 1):
                # Add the product of the probability and the number of stones in the box to the expected value
                expected_value += prob[i] * num_stones[i]
            # Return the expected value
            return expected_value

def f2(...):
    # Calculate the expected value of the number of stones in all boxes
    expected_value = f1(n, q)
    # Calculate the denominator of the expected value
    denominator = f1(n, q - 1)
    # Return the expected value modulo 10^9 + 7
    return expected_value * pow(denominator, -1, 1000000007)

if __name__ == '__main__':
    n, q = map(int, input().split())
    print(f2(n, q))

