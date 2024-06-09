
def get_least_number_of_digits(n):
    # Initialize a list to store the addends
    addends = []
    # Initialize a variable to store the current addend
    current_addend = 1
    # Loop through the digits of n
    for digit in str(n):
        # If the current digit is 1, add it to the current addend
        if digit == "1":
            current_addend *= 10
        # If the current digit is not 1, add the current addend to the list and reset the current addend to 1
        else:
            addends.append(current_addend)
            current_addend = 1
    # Add the last addend to the list
    addends.append(current_addend)
    # Return the sum of the addends
    return sum(addends)

def main():
    n = int(input("Enter a positive integer: "))
    print(get_least_number_of_digits(n))

if __name__ == '__main__':
    main()

