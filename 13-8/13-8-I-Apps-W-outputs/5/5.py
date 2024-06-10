
def get_substring_count(T, N):
    # Initialize variables
    count = 0
    substring = ""

    # Loop through the string S
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

    # Call the function to get the substring count
    count = get_substring_count(T, N)

    # Print the result
    print(count)

if __name__ == '__main__':
    main()

