
def solve(phone_books):
    # Initialize an empty dictionary to store the phone numbers
    phone_numbers = {}

    # Iterate over the phone books
    for phone_book in phone_books:
        # Split the phone book into name and phone numbers
        name, *numbers = phone_book.split()

        # If the name is not already in the dictionary, add it and its phone numbers
        if name not in phone_numbers:
            phone_numbers[name] = set(numbers)
        # Otherwise, add the phone numbers to the existing set
        else:
            phone_numbers[name].update(numbers)

    # Iterate over the dictionary and print the phone numbers for each name
    for name, numbers in phone_numbers.items():
        print(name, len(numbers), *numbers)

solve([
    "ivan 1 00123",
    "masha 1 00123",
    "karl 2 612 12",
    "petr 1 12",
    "katya 1 612",
    "ivan 2 456 456",
    "ivan 8 789 3 23 6 56 9 89 2",
    "dasha 2 23 789"
])

