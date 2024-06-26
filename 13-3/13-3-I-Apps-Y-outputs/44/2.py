
def get_maximal_string(n, k):
    
    # Initialize an array to store the frequencies of each letter
    freq = [0] * 26
    # Initialize a string to store the result
    result = ""
    # Loop until the string is of the desired length
    while len(result) < n:
        # Find the letter with the minimum frequency
        min_freq = min(freq)
        # Find the index of the letter with the minimum frequency
        min_index = freq.index(min_freq)
        # Add the letter to the result string
        result += chr(ord('a') + min_index)
        # Increment the frequency of the letter
        freq[min_index] += 1
    # Return the result string
    return result

def get_query_result(n, k):
    
    # Construct the string
    result = get_maximal_string(n, k)
    # Return the result
    return result

def main():
    # Read the number of queries
    t = int(input())
    # Loop through the queries
    for _ in range(t):
        # Read the query
        n, k = map(int, input().split())
        # Get the result for the query
        result = get_query_result(n, k)
        # Print the result
        print(result)

if __name__ == '__main__':
    main()

