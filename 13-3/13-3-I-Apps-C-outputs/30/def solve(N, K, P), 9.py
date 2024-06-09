
def solve(N, K, P):
    # Initialize a list to store the possible characters
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Initialize a list to store the final string
    string = []
    
    # Iterate through the possible characters and check if the string is valid
    for i in range(K):
        for char in chars:
            # Check if the string is valid
            if len(string) == N and len(set(string)) == K and max(len(string), len(string[::-1])) == P:
                return "".join(string)
            
            # Add the character to the string and check if it is valid
            string.append(char)
    
    # If no valid string is found, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

