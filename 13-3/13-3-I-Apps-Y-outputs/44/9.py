
def get_maximal_string(n, k):
    
    # Initialize an array to store the frequencies of each letter
    freq = [0] * 26
    # Initialize a string to store the result
    result = ""
    # Loop through each letter of the Latin alphabet
    for letter in range(0, 26):
        # If the current letter has not been used yet
        if freq[letter] == 0:
            # Add the current letter to the result string
            result += chr(letter + ord('a'))
            # Increment the frequency of the current letter
            freq[letter] += 1
            # Decrement the number of letters remaining to be used
            k -= 1
        # If the current letter has already been used
        else:
            # Find the next letter that has not been used yet
            for next_letter in range(letter + 1, 26):
                if freq[next_letter] == 0:
                    # Add the next letter to the result string
                    result += chr(next_letter + ord('a'))
                    # Increment the frequency of the next letter
                    freq[next_letter] += 1
                    # Decrement the number of letters remaining to be used
                    k -= 1
                    break
    # If there are still letters remaining to be used
    if k > 0:
        # Add the remaining letters to the result string in alphabetical order
        for letter in range(0, 26):
            if freq[letter] == 0:
                result += chr(letter + ord('a'))
                k -= 1
                if k == 0:
                    break
    return result

def get_maximal_strings(n, k):
    
    # Initialize an empty list to store the results
    results = []
    # Loop through each permutation of the first k letters of the Latin alphabet
    for permutation in itertools.permutations(range(0, k)):
        # Construct a string from the current permutation
        result = ""
        for letter in permutation:
            result += chr(letter + ord('a'))
        # Add the current string to the list of results
        results.append(result)
    return results

def solve(n, k):
    
    # If the number of letters is less than or equal to the number of letters in the Latin alphabet
    if n <= 26:
        # Return any permutation of the first n letters of the Latin alphabet
        return get_maximal_strings(n, k)
    # If the number of letters is greater than the number of letters in the Latin alphabet
    else:
        # Construct a string that maximizes the minimal frequency of any letter
        result = get_maximal_string(n, k)
        # Return the constructed string
        return [result]

if __name__ == '__main__':
    # Read the number of queries from stdin
    t = int(input())
    # Loop through each query
    for _ in range(t):
        # Read the number of letters and the number of letters to use from stdin
        n, k = map(int, input().split())
        # Solve the query and print the result to stdout
        print(*solve(n, k))

