
def check_prefix(phone_number):
    prefix = phone_number[:3]
    if prefix == "555":
        return 1
    else:
        return 0

def main():
    phone_number = input("Enter a seven-digit telephone number: ")
    if len(phone_number) != 7:
        print("Invalid input")
    else:
        result = check_prefix(phone_number)
        if result == 1:
            print("The number should be routed to the directory information operator")
        else:
            print("The number should not be routed to the directory information operator")

if __name__ == '__main__':
    main()

