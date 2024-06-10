
def get_original_string(code_string):
    original_string = ""
    code_list = code_string.split("-")
    for element in code_list:
        if "+" in element:
            num, word = element.split("+")
            original_string += word * int(num)
        else:
            original_string += element
    return original_string

def check_palindrome(original_string):
    return original_string == original_string[::-1]

def main():
    code_string = input("Enter code string: ")
    original_string = get_original_string(code_string)
    if check_palindrome(original_string):
        print("Return")
    else:
        print("Continue")

if __name__ == '__main__':
    main()

