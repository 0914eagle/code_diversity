
def f1(n):
    return n

def f2(s):
    # Initialize variables
    max_length = 0
    current_length = 0
    prev_char = None

    # Iterate through the string
    for char in s:
        # If the current character is different from the previous character
        if char != prev_char:
            # Increment the current length
            current_length += 1
        else:
            # If the current length is greater than the maximum length
            if current_length > max_length:
                # Update the maximum length
                max_length = current_length
            # Reset the current length
            current_length = 1
        # Update the previous character
        prev_char = char

    # If the current length is greater than the maximum length
    if current_length > max_length:
        # Update the maximum length
        max_length = current_length

    # Return the maximum length
    return max_length

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f2(s))

