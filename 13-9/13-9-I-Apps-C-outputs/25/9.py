
def lossy_sort(numbers, m):
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize a dictionary to keep track of the number of digits changed for each number
    digits_changed = {number: 0 for number in numbers}
    
    # Loop through the numbers and check if they are sorted
    for i in range(len(numbers)):
        # If the current number is not sorted, find the smallest number that is greater than it
        if sorted_numbers[i] != numbers[i]:
            # Find the index of the smallest number that is greater than the current number
            j = i + 1
            while j < len(numbers) and sorted_numbers[j] <= numbers[i]:
                j += 1
            
            # Swap the current number with the smallest number that is greater than it
            numbers[i], numbers[j] = numbers[j], numbers[i]
            
            # Increment the number of digits changed for the current number
            digits_changed[numbers[i]] += 1
    
    # Return the sorted numbers and the minimum number of digits changed
    return sorted_numbers, min(digits_changed.values())

def main():
    n, m = map(int, input().split())
    numbers = []
    for _ in range(n):
        numbers.append(int(input()))
    sorted_numbers, digits_changed = lossy_sort(numbers, m)
    print(*sorted_numbers)
    print(digits_changed)

if __name__ == '__main__':
    main()

