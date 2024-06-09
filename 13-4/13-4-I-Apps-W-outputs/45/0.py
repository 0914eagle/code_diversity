
def f1(string):
    # Initialize variables
    output = ""
    backspace_count = 0
    home_count = 0
    end_count = 0

    # Iterate through the string
    for char in string:
        # If the character is a letter or digit, add it to the output
        if char.isalpha() or char.isdigit():
            output += char
        # If the character is a space, add a space to the output
        elif char == " ":
            output += " "
        # If the character is '<', decrement the backspace count
        elif char == "<":
            backspace_count -= 1
        # If the character is '[', increment the home count
        elif char == "[":
            home_count += 1
        # If the character is ']', increment the end count
        elif char == "]":
            end_count += 1

    # If the backspace count is negative, move the cursor to the end of the string
    if backspace_count < 0:
        end_count += backspace_count
        backspace_count = 0

    # If the home count is positive, move the cursor to the beginning of the string
    if home_count > 0:
        output = ""
        home_count = 0

    # If the end count is positive, move the cursor to the end of the string
    if end_count > 0:
        output = output[::-1]
        end_count = 0

    # Return the final output
    return output

def f2(string):
    # Initialize variables
    output = ""
    backspace_count = 0
    home_count = 0
    end_count = 0

    # Iterate through the string
    for char in string:
        # If the character is a letter or digit, add it to the output
        if char.isalpha() or char.isdigit():
            output += char
        # If the character is a space, add a space to the output
        elif char == " ":
            output += " "
        # If the character is '<', decrement the backspace count
        elif char == "<":
            backspace_count -= 1
        # If the character is '[', increment the home count
        elif char == "[":
            home_count += 1
        # If the character is ']', increment the end count
        elif char == "]":
            end_count += 1

    # If the backspace count is negative, move the cursor to the end of the string
    if backspace_count < 0:
        end_count += backspace_count
        backspace_count = 0

    # If the home count is positive, move the cursor to the beginning of the string
    if home_count > 0:
        output = ""
        home_count = 0

    # If the end count is positive, move the cursor to the end of the string
    if end_count > 0:
        output = output[::-1]
        end_count = 0

    # Return the final output
    return output

if __name__ == '__main__':
    # Get the number of test cases
    num_test_cases = int(input())

    # Iterate through the test cases
    for _ in range(num_test_cases):
        # Get the input string
        string = input()

        # Call the appropriate function based on the length of the string
        if len(string) <= 1000:
            output = f1(string)
        else:
            output = f2(string)

        # Print the output
        print(output)

