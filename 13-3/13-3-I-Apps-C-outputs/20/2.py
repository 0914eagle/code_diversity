
def get_max_guests(apartment_layout):
    # Initialize variables
    max_guests = 0
    table_size = 0

    # Iterate through the apartment layout
    for row in apartment_layout:
        for col in row:
            # If the current square is free, increment the table size
            if col == ".":
                table_size += 1
            # If the current square is blocked, check if the table size is greater than the maximum number of guests
            elif col == "X":
                if table_size > max_guests:
                    max_guests = table_size
                # Reset the table size
                table_size = 0

    # Return the maximum number of guests
    return max_guests

def main():
    # Read the apartment layout from stdin
    apartment_layout = []
    for _ in range(int(input())):
        apartment_layout.append(input())

    # Call the function to get the maximum number of guests
    max_guests = get_max_guests(apartment_layout)

    # Print the result
    print(max_guests)

if __name__ == '__main__':
    main()

