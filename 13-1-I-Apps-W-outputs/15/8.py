
def solve(s):
    # Initialize the number of operations to 0
    k = 0
    
    # Loop until the string is a palindrome or the maximum number of operations is reached
    while not is_palindrome(s) and k < 30:
        # Check if the string can be made a palindrome by reversing the first half and appending it to the end
        if can_reverse_first_half(s):
            s = reverse_first_half(s)
            k += 1
            print("R", len(s) // 2)
        # Check if the string can be made a palindrome by reversing the second half and appending it to the beginning
        elif can_reverse_second_half(s):
            s = reverse_second_half(s)
            k += 1
            print("L", len(s) // 2)
        # If neither of the above conditions are met, the string cannot be made a palindrome
        else:
            break
    
    # Return the number of operations performed
    return k

# Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Check if a string can be made a palindrome by reversing the first half and appending it to the end
def can_reverse_first_half(s):
    return len(s) % 2 == 1 and s[:len(s) // 2] == s[:len(s) // 2][::-1]

# Reverse the first half of a string and append it to the end
def reverse_first_half(s):
    return s + s[:len(s) // 2][::-1]

# Check if a string can be made a palindrome by reversing the second half and appending it to the beginning
def can_reverse_second_half(s):
    return len(s) % 2 == 1 and s[len(s) // 2:] == s[len(s) // 2:][::-1]

# Reverse the second half of a string and append it to the beginning
def reverse_second_half(s):
    return s[len(s) // 2:][::-1] + s

