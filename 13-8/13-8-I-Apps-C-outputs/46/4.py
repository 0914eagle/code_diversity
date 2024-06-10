
def solve(queries):
    # Initialize an empty string to store the answers
    answers = ""
    
    # Iterate through each query
    for query in queries:
        # Get the current string and the index of the character to find
        string, index = query
        
        # If the index is 1, the answer is the first character of the string
        if index == 1:
            answers += string[0]
        # If the index is greater than 1, find the k-th character of the string
        else:
            # Initialize a variable to store the current string
            current_string = string
            
            # Iterate through each index
            for i in range(2, index+1):
                # Find the k-th character of the current string
                current_string = current_string[current_string.find(string)+1:]
            
            # Add the answer to the answers string
            answers += current_string[0]
    
    # Return the answers string
    return answers

def main():
    # Read the number of queries
    queries = int(input())
    
    # Read the queries
    queries = [input().split() for _ in range(queries)]
    
    # Solve the queries
    answers = solve(queries)
    
    # Print the answers
    print(answers)

if __name__ == '__main__':
    main()

