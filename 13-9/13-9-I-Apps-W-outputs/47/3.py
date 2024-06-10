
def is_palindrome(string):
    return string == string[::-1]

def decode_string(code_string):
    original_string = ""
    while code_string:
        if code_string[0].isdigit():
            count = int(code_string[0])
            code_string = code_string[1:]
            if code_string[0] == "+":
                original_string += code_string[1:code_string.index("-")] * count
                code_string = code_string[code_string.index("-")+1:]
            else:
                original_string += code_string[0] * count
                code_string = code_string[1:]
        else:
            original_string += code_string[0]
            code_string = code_string[1:]
    return original_string

def main():
    code_string = input()
    original_string = decode_string(code_string)
    if is_palindrome(original_string):
        print("Return")
    else:
        print("Continue")

if __name__ == '__main__':
    main()

