
def is_directory_number(number):
    prefix = number[:3]
    return prefix == "555"

def main():
    number = input("Enter a seven-digit telephone number: ")
    if len(number) != 7:
        print("Invalid input")
        return
    if is_directory_number(number):
        print("1")
    else:
        print("0")

if __name__ == '__main__':
    main()

