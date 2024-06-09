
def get_maximal_string(n, k):
    
    # Initialize an array to store the frequencies of each letter
    freq = [0] * 26
    # Initialize a string to store the result
    result = ""
    # Loop through each letter of the Latin alphabet
    for letter in range(0, 26):
        # If the letter has not been used yet
        if freq[letter] == 0:
            # Add the letter to the result string
            result += chr(letter + ord('a'))
            # Increment the frequency of the letter
            freq[letter] += 1
            # Decrement the number of letters left to use
            k -= 1
        # If the letter has already been used
        else:
            # Find the letter with the minimum frequency
            min_freq = min(freq)
            # Find the index of the letter with the minimum frequency
            min_index = freq.index(min_freq)
            # Add the letter to the result string
            result += chr(min_index + ord('a'))
            # Increment the frequency of the letter
            freq[min_index] += 1
            # Decrement the number of letters left to use
            k -= 1
        # If all letters have been used
        if k == 0:
            # Break out of the loop
            break
    # Return the result string
    return result

def get_query_result(n, k):
    
    # Call the get_maximal_string function to get the result string
    result = get_maximal_string(n, k)
    # Return the result string
    return result

def main():
    # Read the number of queries from stdin
    t = int(input())
    # Loop through each query
    for _ in range(t):
        # Read the query from stdin
        n, k = map(int, input().split())
        # Call the get_query_result function to get the result for this query
        result = get_query_result(n, k)
        # Print the result
        print(result)

if __name__ == '__main__':
    main()

