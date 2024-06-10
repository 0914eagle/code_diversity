
def solve(s):
    # Initialize variables
    n = len(s)
    count = 0
    i = 0
    
    # Loop through the string
    while i < n:
        # If the current character is not the same as the next character
        if s[i] != s[i+1]:
            # Increment the count
            count += 1
        # If the current character is the same as the next character
        else:
            # Find the length of the consecutive characters
            length = 1
            j = i + 1
            while j < n and s[j] == s[i]:
                length += 1
                j += 1
            # Increment the count by the length of the consecutive characters
            count += length
            # Set i to the index after the consecutive characters
            i = j
    
    # Return the count
    return count

def main():
    # Read the input
    n = int(input())
    s = input()
    
    # Call the solve function
    count = solve(s)
    
    # Print the output
    print(count)

if __name__ == '__main__':
    main()

