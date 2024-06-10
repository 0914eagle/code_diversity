
def is_routable_to_directory_information(phone_number):
    prefix = phone_number[:3]
    return prefix == "555"

def main():
    phone_number = input("Enter a seven-digit telephone number: ")
    if len(phone_number) != 7:
        print("Invalid phone number")
        return
    if is_routable_to_directory_information(phone_number):
        print("1")
    else:
        print("0")

if __name__ == '__main__':
    main()

