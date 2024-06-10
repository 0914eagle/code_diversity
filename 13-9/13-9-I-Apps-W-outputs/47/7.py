
def get_original_string(code_string):
    original_string = ""
    current_string = ""
    repeat_count = 0
    for char in code_string:
        if char.isdigit():
            repeat_count = int(char)
        elif char == '+':
            current_string = ""
        elif char == '-':
            original_string += current_string * repeat_count
        else:
            current_string += char
    
    if repeat_count != 0:
        original_string += current_string * repeat_count
    
    return original_string

def is_palindrome(string):
    return string == string[::-1]

def main():
    code_string = input("Enter code string: ")
    original_string = get_original_string(code_string)
    if is_palindrome(original_string):
        print("Return")
    else:
        print("Continue")

if __name__ == '__main__':
    main()

