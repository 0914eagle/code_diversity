
def decode_string(code_string):
    original_string = ""
    code_list = code_string.split("-")
    for code in code_list:
        if "+" in code:
            num, word = code.split("+")
            original_string += word * int(num)
        else:
            original_string += code
    return original_string

def is_palindrome(string):
    return string == string[::-1]

def main():
    code_string = input("Enter the code string: ")
    original_string = decode_string(code_string)
    if is_palindrome(original_string):
        print("Return")
    else:
        print("Continue")

if __name__ == '__main__':
    main()

