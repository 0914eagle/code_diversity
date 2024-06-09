
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

    # Iterate over the phone numbers and remove duplicates
    for name, numbers in phone_numbers.items():
        phone_numbers[name] = list(set(numbers))

    # Sort the phone numbers for each name
    for name, numbers in phone_numbers.items():
        phone_numbers[name].sort()

    # Return the phone numbers in the required format
    return "{}".format("\n".join(["{} {} {}".format(name, len(numbers), " ".join(numbers)) for name, numbers in phone_numbers.items()]))

