
import math

def get_expected_value(n, queries):
    # Initialize the number of stones in each box to 0
    num_stones = [0] * (n + 1)
    
    # Loop through each query
    for query in queries:
        # If the query is of type 1, insert a stone into the box between u and v
        if query[0] == 1:
            num_stones[query[1]] += 1
            num_stones[query[2]] += 1
        # If the query is of type 2, calculate the expected value of A
        elif query[0] == 2:
            # Calculate the sum of the squares of the number of stones in each box
            sum_squares = sum([x**2 for x in num_stones])
            # Calculate the expected value of A
            expected_value = sum_squares / n
    
    # Return the expected value of A
    return expected_value

def main():
    # Read the input
    n, q = map(int, input().split())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    
    # Calculate the expected value of A
    expected_value = get_expected_value(n, queries)
    
    # Print the result
    print(expected_value)

if __name__ == '__main__':
    main()

