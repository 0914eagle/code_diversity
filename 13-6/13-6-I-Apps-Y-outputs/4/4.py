
def get_remainder(n, x, y, number):
    # Initialize the minimum number of operations to perform
    min_operations = 0
    # Initialize the current number
    current_number = number
    # Loop through each digit of the number
    for i in range(n):
        # If the current digit is 0, change it to 1 and increment the minimum number of operations
        if current_number[i] == "0":
            current_number = current_number[:i] + "1" + current_number[i+1:]
            min_operations += 1
        # If the current digit is 1 and the current index is greater than or equal to x, change it to 0 and increment the minimum number of operations
        elif current_number[i] == "1" and i >= x:
            current_number = current_number[:i] + "0" + current_number[i+1:]
            min_operations += 1
    # Return the minimum number of operations to perform
    return min_operations

def main():
    # Read the input
    n, x, y = map(int, input().split())
    number = input()
    # Call the get_remainder function and print the result
    print(get_remainder(n, x, y, number))

if __name__ == '__main__':
    main()

