
def get_min_operations(s):
    # Initialize a variable to store the minimum number of operations
    min_operations = 0
    # Loop through the string and check if there are any consecutive characters that are the same
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            # If there are consecutive characters that are the same, delete them and increment the minimum number of operations
            min_operations += 1
            # Delete the consecutive characters
            s = s[:i] + s[i+2:]
    # Return the minimum number of operations
    return min_operations

def main():
    # Read the input string
    s = input()
    # Call the get_min_operations function and print the result
    print(get_min_operations(s))

if __name__ == '__main__':
    main()

