
def solve(phone_books):
    # Initialize an empty dictionary to store the phone numbers
    phone_numbers = {}

    # Iterate over the phone books
    for phone_book in phone_books:
        # Split the phone book into name and phone numbers
        name, *numbers = phone_book.split()

        # Initialize an empty list to store the phone numbers for the current name
        if name not in phone_numbers:
            phone_numbers[name] = []

        # Add the phone numbers to the list
        for number in numbers:
            phone_numbers[name].append(number)

    # Sort the phone numbers for each name
    for name in phone_numbers:
        phone_numbers[name].sort()

    # Print the organized information about the phone numbers
    print(len(phone_numbers))
    for name, numbers in phone_numbers.items():
        print(f"{name} {len(numbers)} {' '.join(numbers)}")

