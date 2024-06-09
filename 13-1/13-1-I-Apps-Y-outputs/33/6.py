
def get_maximal_string(n, k):
    
    # Initialize an array to store the frequencies of each letter
    freq = [0] * 26
    # Initialize a string to store the result
    result = ""
    # Loop through each letter of the Latin alphabet
    for i in range(0, 26):
        # If the current letter has not been used yet
        if freq[i] == 0:
            # Add the current letter to the result string
            result += chr(i + ord('a'))
            # Increment the frequency of the current letter
            freq[i] += 1
            # Decrement the number of letters left to use
            k -= 1
        # If the current letter has already been used
        else:
            # Find the next letter that has not been used yet
            for j in range(i + 1, 26):
                if freq[j] == 0:
                    # Add the next letter to the result string
                    result += chr(j + ord('a'))
                    # Increment the frequency of the next letter
                    freq[j] += 1
                    # Decrement the number of letters left to use
                    k -= 1
                    break
    # If there are still letters left to use
    if k > 0:
        # Loop through the result string and add additional letters as needed
        for i in range(len(result), n):
            for j in range(0, 26):
                if freq[j] == 0:
                    result += chr(j + ord('a'))
                    freq[j] += 1
                    k -= 1
                    if k == 0:
                        break
            if k == 0:
                break
    return result

def get_maximal_strings(queries):
    
    results = []
    for query in queries:
        results.append(get_maximal_string(query[0], query[1]))
    return results

if __name__ == '__main__':
    queries = []
    for _ in range(int(input())):
        queries.append(tuple(map(int, input().split())))
    results = get_maximal_strings(queries)
    for result in results:
        print(result)

