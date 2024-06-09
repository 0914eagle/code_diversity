
def is_palindrome(string):
    return string == string[::-1]

def main():
    string = input("Enter a string: ")
    if is_palindrome(string):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

