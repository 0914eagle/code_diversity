
def get_number_of_occurences(N, T):
    # Initialize a counter for the number of occurences
    count = 0
    
    # Initialize a string S that is the concatenation of 10^10 copies of the string 110
    S = "110" * 10**10
    
    # Loop through each substring of S that is of length N
    for i in range(len(S) - N + 1):
        # Check if the substring is equal to T
        if S[i:i+N] == T:
            # Increment the counter if it is
            count += 1
    
    # Return the number of occurences
    return count

def main():
    # Read the input from stdin
    N = int(input())
    T = input()
    
    # Call the function and print the result
    print(get_number_of_occurences(N, T))

if __name__ == '__main__':
    main()

