
def get_original_string(code_string):
    original_string = ""
    code_list = code_string.split("-")
    for code in code_list:
        if "+" in code:
            integer, string = code.split("+")
            original_string += string * int(integer)
        else:
            original_string += code
    return original_string

def check_palindrome(original_string):
    return original_string == original_string[::-1]

def main():
    code_string = input("Enter the code string: ")
    original_string = get_original_string(code_string)
    if check_palindrome(original_string):
        print("Return")
    else:
        print("Continue")

if __name__ == '__main__':
    main()

