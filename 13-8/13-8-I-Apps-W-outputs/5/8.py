
def count_occurrences(T, N):
    # Initialize a counter for the number of occurrences
    count = 0
    
    # Loop through the string S and check if T occurs as a contiguous substring
    for i in range(len(S) - N + 1):
        if S[i:i+N] == T:
            count += 1
    
    # Return the number of occurrences
    return count

def main():
    # Read the input from stdin
    N = int(input())
    T = input()
    
    # Call the count_occurrences function and print the result
    print(count_occurrences(T, N))

if __name__ == '__main__':
    main()

