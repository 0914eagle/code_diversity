
def get_original_string(code_string):
    original_string = ""
    for char in code_string:
        if char.isdigit():
            repeat_count = int(char)
            char = code_string[code_string.index(char) + 1]
            original_string += char * repeat_count
        else:
            original_string += char
    return original_string

def is_palindrome(string):
    return string == string[::-1]

def solve(code_string):
    original_string = get_original_string(code_string)
    if is_palindrome(original_string):
        return "Return"
    else:
        return "Continue"

if __name__ == '__main__':
    code_string = input()
    print(solve(code_string))

