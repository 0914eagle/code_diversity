
def get_hours_until_new_year(m):
    # Calculate the hours until New Year at m o'clock on December 30th
    hours_until_new_year = 24 - m
    return hours_until_new_year

def main():
    # Accept input from the user
    m = int(input("Enter the hour (in 24-hour notation): "))

    # Check if the input is valid
    if m < 1 or m > 23:
        print("Invalid input. Please enter an integer between 1 and 23.")
        return

    # Calculate the hours until New Year
    hours_until_new_year = get_hours_until_new_year(m)

    # Print the result
    print(f"We have {hours_until_new_year} hours until New Year at {m}:00 on December 30th.")

if __name__ == '__main__':
    main()

