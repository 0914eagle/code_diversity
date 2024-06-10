
def delete_substring(s):
    # Initialize variables
    n = len(s)
    count = 0
    
    # Iterate through the string
    for i in range(n):
        # If the current character is not equal to the next character
        if s[i] != s[i+1]:
            # Increment the count
            count += 1
    
    # Return the count
    return count

def minimum_operations(s):
    # Initialize variables
    n = len(s)
    count = 0
    
    # Iterate through the string
    for i in range(n):
        # If the current character is not equal to the next character
        if s[i] != s[i+1]:
            # Increment the count
            count += 1
    
    # Return the count
    return count

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(minimum_operations(s))

