
def solve(n, k):
    # Initialize a list to store the letters
    letters = []
    # Loop through the number of letters
    for i in range(1, k+1):
        # Append the letters of the alphabet
        letters.append(chr(i + 96))
    # Initialize a string to store the answer
    answer = ""
    # Loop through the length of the string
    for i in range(n):
        # Append a letter to the answer
        answer += letters[i % k]
    # Return the answer
    return answer

