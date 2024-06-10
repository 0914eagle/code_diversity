
def convert_string(code_string):
    original_string = ""
    for i in range(len(code_string)):
        if code_string[i].isdigit():
            num = int(code_string[i])
            j = i + 1
            while j < len(code_string) and code_string[j] != '-':
                original_string += code_string[j]
                j += 1
            i = j
        else:
            original_string += code_string[i]
    return original_string

def is_palindrome(string):
    return string == string[::-1]

def main():
    code_string = input("Enter code string: ")
    original_string = convert_string(code_string)
    if is_palindrome(original_string):
        print("Return")
    else:
        print("Continue")

if __name__ == '__main__':
    main()

