
def get_min_digit_changes(numbers, m):
    # Initialize a count of digit changes to 0
    digit_changes = 0
    
    # Loop through the numbers and compare adjacent pairs
    for i in range(len(numbers) - 1):
        # If the current number is greater than the next number, increment the digit changes
        if numbers[i] > numbers[i + 1]:
            digit_changes += 1
    
    # Return the minimum number of digit changes needed to sort the numbers
    return digit_changes

def sort_numbers(numbers, m):
    # Initialize a sorted list of numbers
    sorted_numbers = []
    
    # Loop through the numbers and add them to the sorted list in sorted order
    for i in range(len(numbers)):
        # Find the smallest number that is greater than or equal to the current number
        smallest_greater = float('inf')
        for j in range(len(sorted_numbers)):
            if sorted_numbers[j] >= numbers[i] and smallest_greater > sorted_numbers[j]:
                smallest_greater = sorted_numbers[j]
        
        # Add the current number to the sorted list
        sorted_numbers.append(smallest_greater)
    
    # Return the sorted list of numbers
    return sorted_numbers

def main():
    # Read the input
    n, m = map(int, input().split())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    
    # Call the functions to get the minimum digit changes and sort the numbers
    min_digit_changes = get_min_digit_changes(numbers, m)
    sorted_numbers = sort_numbers(numbers, m)
    
    # Print the minimum digit changes and the sorted list of numbers
    print(min_digit_changes)
    for number in sorted_numbers:
        print(number)

if __name__ == '__main__':
    main()

