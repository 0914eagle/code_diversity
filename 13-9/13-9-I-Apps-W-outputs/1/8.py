
def delete_string(s):
    # Initialize a variable to store the result
    result = 0
    
    # Loop through the string and check if there are any equal consecutive characters
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            # If there are, delete the consecutive characters and update the result
            result += 1
            s = s[:i] + s[i + 2:]
    
    # Return the result
    return result

def main():
    # Take input from the user
    n = int(input())
    s = input()
    
    # Calculate the minimum number of operations to delete the string
    result = delete_string(s)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

