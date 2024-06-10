
def get_next_string(s):
    # Initialize an empty string to store the next string
    next_string = ""
    
    # Iterate through the characters in the input string
    for c in s:
        # If the current character is a digit, append it to the next string
        if c.isdigit():
            next_string += c
        # If the current character is not a digit, append it to the next string twice
        else:
            next_string += c * 2
    
    # Return the next string
    return next_string

def get_string_after_days(s, days):
    # Initialize a variable to store the current string
    current_string = s
    
    # Iterate through the days
    for _ in range(days):
        # Get the next string by applying the transformation rule
        current_string = get_next_string(current_string)
    
    # Return the current string
    return current_string

def get_kth_character(s, k):
    # Return the k-th character from the left in the string
    return s[k - 1]

if __name__ == '__main__':
    s = input()
    k = int(input())
    days = 5 * (10 ** 15)
    string_after_days = get_string_after_days(s, days)
    kth_character = get_kth_character(string_after_days, k)
    print(kth_character)

