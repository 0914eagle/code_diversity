
def is_palindrome(string):
    return string == string[::-1]

def main():
    input_string = input("Enter a string: ")
    if is_palindrome(input_string):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

