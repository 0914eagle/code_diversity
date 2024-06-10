
def get_substring_count(N, T):
    # Initialize variables
    count = 0
    substring = ""
    
    # Iterate through the string S
    for i in range(N):
        # Append the next character to the substring
        substring += T[i % len(T)]
        
        # If the substring is equal to T, increment the count
        if substring == T:
            count += 1
    
    # Return the count
    return count

def main():
    # Read the input
    N = int(input())
    T = input()
    
    # Call the function and print the result
    print(get_substring_count(N, T))

if __name__ == '__main__':
    main()

