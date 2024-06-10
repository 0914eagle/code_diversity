
def find_occurrences(T, N):
    # Initialize a counter for the number of occurrences
    count = 0
    
    # Loop through the concatenation of 10^10 copies of the string 110
    for i in range(10**10):
        # Check if the substring T occurs at the current position
        if T == S[i:i+N]:
            # Increment the counter
            count += 1
    
    # Return the number of occurrences
    return count

def main():
    # Read the input from stdin
    N = int(input())
    T = input()
    
    # Call the find_occurrences function and print the result
    print(find_occurrences(T, N))

if __name__ == '__main__':
    main()

