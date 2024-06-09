
def get_maximum_income(numbers, k):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    
    # Initialize the maximum income and the current income
    maximum_income = 0
    current_income = sum(numbers)
    
    # Loop through the numbers and perform the specified number of swaps
    for i in range(k):
        # Find the index of the largest number that has not been swapped
        largest_index = 0
        for j in range(1, len(numbers)):
            if numbers[j] > numbers[largest_index]:
                largest_index = j
                
        # Swap the largest number with the next number
        numbers[largest_index], numbers[largest_index + 1] = numbers[largest_index + 1], numbers[largest_index]
        
        # Update the current income
        current_income += numbers[largest_index]
        
        # Update the maximum income
        maximum_income = max(maximum_income, current_income)
    
    # Return the maximum income
    return maximum_income

def main():
    # Read the input
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    # Get the maximum income
    maximum_income = get_maximum_income(numbers, k)
    
    # Print the result
    print(maximum_income)

if __name__ == '__main__':
    main()

