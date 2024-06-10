
def is_directory_number(number):
    prefix = int(number[:3])
    if prefix == 555:
        return 1
    else:
        return 0

def main():
    number = input("Enter a seven-digit telephone number: ")
    print(is_directory_number(number))

if __name__ == '__main__':
    main()

