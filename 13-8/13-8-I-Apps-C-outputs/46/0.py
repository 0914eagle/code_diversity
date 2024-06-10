
def solve(queries):
    # Initialize the first string
    f = "What are you doing at the end of the world? Are you busy? Will you save us?"
    
    # Iterate over the queries
    for query in queries:
        # Get the current string and the index of the character to be retrieved
        current_string, index = query
        
        # Check if the index is valid
        if index > len(current_string):
            output = '.'
        else:
            # Get the character at the given index
            output = current_string[index - 1]
        
        # Update the current string
        current_string = "What are you doing while sending \"" + current_string + "\"? Are you busy? Will you send \"" + current_string + "\"?"
        
        # Print the output
        print(output, end='')
    
    return

if __name__ == '__main__':
    q = int(input())
    queries = []
    
    for i in range(q):
        n, k = map(int, input().split())
        queries.append((f[n], k))
    
    solve(queries)

