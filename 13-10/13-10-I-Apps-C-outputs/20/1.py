
def get_answers(queries):
    # Initialize a dictionary to store the answers
    answers = {}
    
    # Iterate over the queries
    for query in queries:
        # Get the start and end values of the interval
        start, end = query
        
        # Initialize a variable to store the number of appearances
        num_appearances = 0
        
        # Iterate over the rows of the table
        for i in range(1, end + 1):
            # Get the value of the current cell
            value = get_value(i, start)
            
            # If the value is in the interval, increment the number of appearances
            if value >= start and value <= end:
                num_appearances += 1
        
        # Add the answer to the dictionary
        answers[query] = num_appearances
    
    # Return the answers
    return answers

def get_value(i, j):
    # Base case: If j is 1, return the ordinal number of the row
    if j == 1:
        return i
    
    # Recursive case: Return the value of the cell to the left plus the reverse of the value of the cell to the left
    return get_value(i, j - 1) + int(str(get_value(i, j - 1))[::-1])

def main():
    # Read the number of queries
    num_queries = int(input())
    
    # Read the queries
    queries = []
    for _ in range(num_queries):
        queries.append(tuple(map(int, input().split())))
    
    # Get the answers
    answers = get_answers(queries)
    
    # Print the answers
    for query, answer in answers.items():
        print(answer)

if __name__ == '__main__':
    main()

