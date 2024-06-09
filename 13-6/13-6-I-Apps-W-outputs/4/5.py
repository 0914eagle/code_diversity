
def solve_queries(queries):
    # Initialize the set and the maximum possible value
    set_ = []
    max_value = 0
    
    # Iterate over the queries
    for query in queries:
        # If the query is of type 1, add the number to the set
        if query[0] == 1:
            set_.append(query[1])
        # If the query is of type 2, find the maximum possible value
        else:
            # Sort the set in descending order
            set_.sort(reverse=True)
            # Initialize the sum and the count of numbers
            sum = 0
            count = 0
            # Iterate over the set
            for num in set_:
                # Add the number to the sum and increment the count
                sum += num
                count += 1
                # If the sum is greater than the maximum possible value, break
                if sum > max_value:
                    break
            # Calculate the maximum possible value
            max_value = sum / count
        
    # Return the maximum possible value
    return max_value

def main():
    # Read the number of queries
    queries_count = int(input())
    
    # Initialize the queries list
    queries = []
    
    # Iterate over the queries
    for _ in range(queries_count):
        # Read the query
        query = list(map(int, input().split()))
        # Add the query to the list
        queries.append(query)
    
    # Solve the queries
    max_value = solve_queries(queries)
    
    # Print the result
    print(max_value)

if __name__ == '__main__':
    main()

