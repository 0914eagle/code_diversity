
def get_sorted_numbers(numbers, m):
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize a counter to keep track of the number of digits changed
    num_digits_changed = 0
    
    # Loop through the sorted numbers and change the digits as necessary
    for i in range(len(sorted_numbers)):
        # If the current number is not equal to the previous number, change the digits
        if sorted_numbers[i] != sorted_numbers[i-1]:
            # Change the digits of the current number to match the previous number
            sorted_numbers[i] = sorted_numbers[i-1]
            # Increment the counter
            num_digits_changed += 1
    
    # Return the sorted numbers and the number of digits changed
    return sorted_numbers, num_digits_changed

def main():
    # Read the input
    n, m = map(int, input().split())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    
    # Get the sorted numbers and the number of digits changed
    sorted_numbers, num_digits_changed = get_sorted_numbers(numbers, m)
    
    # Print the sorted numbers
    for number in sorted_numbers:
        print(str(number).zfill(m))
    
    # Print the number of digits changed
    print(num_digits_changed)

if __name__ == '__main__':
    main()

