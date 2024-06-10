
def get_max_number(v, a):
    # Initialize a list to store the numbers that can be written
    numbers = []
    
    # Iterate through the list of a_i values
    for i in range(len(a)):
        # Check if the current value is less than or equal to the available paint
        if a[i] <= v:
            # Add the current value to the list of numbers that can be written
            numbers.append(i)
    
    # Sort the list of numbers in descending order
    numbers.sort(reverse=True)
    
    # Initialize a variable to store the maximum number that can be written
    max_number = 0
    
    # Iterate through the list of numbers
    for i in range(len(numbers)):
        # Check if the current number is a multiple of 10
        if numbers[i] % 10 == 0 and numbers[i] != 0:
            # Skip this number
            continue
        else:
            # Add the current number to the maximum number that can be written
            max_number += numbers[i] * 10 ** i
    
    # Return the maximum number that can be written
    return max_number

def main():
    # Read the input
    v = int(input())
    a = list(map(int, input().split()))
    
    # Call the get_max_number function and print the result
    print(get_max_number(v, a))

if __name__ == '__main__':
    main()

