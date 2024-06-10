
def is_directory_operator(number):
    if number[:3] == "555":
        return 1
    else:
        return 0

def main():
    number = input("Enter a 7-digit telephone number: ")
    print(is_directory_operator(number))

if __name__ == '__main__':
    main()

