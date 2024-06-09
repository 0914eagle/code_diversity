
def f1(s):
    # Initialize variables
    result = ""
    backspace_count = 0
    home_count = 0
    end_count = 0
    
    # Iterate through the string
    for c in s:
        # If the current character is a letter or a digit, add it to the result
        if c.isalpha() or c.isdigit():
            result += c
        # If the current character is a space, add a space to the result
        elif c == " ":
            result += " "
        # If the current character is a '<', move the backspace_count forward
        elif c == "<":
            backspace_count += 1
        # If the current character is a '[', move the home_count forward
        elif c == "[":
            home_count += 1
        # If the current character is a ']', move the end_count forward
        elif c == "]":
            end_count += 1
    
    # If the backspace_count is odd, remove the last character from the result
    if backspace_count % 2 == 1:
        result = result[:-1]
    
    # If the home_count is odd, move the cursor to the front of the string
    if home_count % 2 == 1:
        result = result[home_count:]
    
    # If the end_count is odd, move the cursor to the back of the string
    if end_count % 2 == 1:
        result = result[:-end_count]
    
    return result

def f2(s):
    # Initialize variables
    result = ""
    backspace_count = 0
    home_count = 0
    end_count = 0
    
    # Iterate through the string
    for c in s:
        # If the current character is a letter or a digit, add it to the result
        if c.isalpha() or c.isdigit():
            result += c
        # If the current character is a space, add a space to the result
        elif c == " ":
            result += " "
        # If the current character is a '<', move the backspace_count forward
        elif c == "<":
            backspace_count += 1
        # If the current character is a '[', move the home_count forward
        elif c == "[":
            home_count += 1
        # If the current character is a ']', move the end_count forward
        elif c == "]":
            end_count += 1
    
    # If the backspace_count is odd, remove the last character from the result
    if backspace_count % 2 == 1:
        result = result[:-1]
    
    # If the home_count is odd, move the cursor to the front of the string
    if home_count % 2 == 1:
        result = result[home_count:]
    
    # If the end_count is odd, move the cursor to the back of the string
    if end_count % 2 == 1:
        result = result[:-end_count]
    
    return result

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        result = f1(s)
        print(result)

