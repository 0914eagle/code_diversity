
def get_maximal_string(n, k):
    
    # Initialize an array to store the frequencies of each letter
    freq = [0] * 26
    # Initialize a string to store the result
    result = ""
    # Loop until the string is of the required length
    while len(result) < n:
        # Find the letter with the minimum frequency
        min_freq_idx = freq.index(min(freq))
        # Add the letter to the result string
        result += chr(ord('a') + min_freq_idx)
        # Increment the frequency of the letter
        freq[min_freq_idx] += 1
    # Return the result string
    return result

def get_query_result(n, k):
    
    # Call the function to get the maximal string
    result = get_maximal_string(n, k)
    # Return the result string
    return result

if __name__ == '__main__':
    # Read the number of queries
    t = int(input())
    # Loop through the queries
    for _ in range(t):
        # Read the query parameters
        n, k = map(int, input().split())
        # Get the result for the query
        result = get_query_result(n, k)
        # Print the result
        print(result)

