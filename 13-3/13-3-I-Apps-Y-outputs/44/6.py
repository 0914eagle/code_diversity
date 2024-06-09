
def get_maximal_string(n, k):
    
    # Initialize an array to store the frequencies of each letter
    freq = [0] * 26
    # Initialize a string to store the result
    result = ""
    # Loop until the string is of the desired length
    while len(result) < n:
        # Loop through each letter of the alphabet
        for letter in range(0, 26):
            # If the frequency of the letter is less than k, add it to the string
            if freq[letter] < k:
                result += chr(letter + ord('a'))
                freq[letter] += 1
                break
    return result

def get_query_result(n, k):
    
    return get_maximal_string(n, k)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(get_query_result(n, k))

