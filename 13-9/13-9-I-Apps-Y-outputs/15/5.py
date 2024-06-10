
def is_directory_number(number):
    prefix = number[:3]
    if prefix == "555":
        return 1
    else:
        return 0

def main():
    number = input("Enter a seven-digit telephone number: ")
    if len(number) != 7:
        print("Invalid input")
        return
    result = is_directory_number(number)
    print(result)

if __name__ == '__main__':
    main()

