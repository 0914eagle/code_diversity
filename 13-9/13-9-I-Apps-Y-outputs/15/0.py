
def check_directory_number(telephone_number):
    prefix = telephone_number[:3]
    if prefix == "555":
        return 1
    else:
        return 0

def main():
    telephone_number = input("Enter a telephone number: ")
    result = check_directory_number(telephone_number)
    print(result)

if __name__ == '__main__':
    main()

