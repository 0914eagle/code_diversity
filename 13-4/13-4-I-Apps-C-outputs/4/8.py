
def get_max_or(numbers, k, x):
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    
    # Initialize the maximum OR value
    max_or = 0
    
    # Loop through the numbers
    for i in range(len(numbers)):
        # Calculate the OR value for the current number
        current_or = 0
        for j in range(i, len(numbers)):
            current_or |= numbers[j]
        
        # If the current OR value is greater than the maximum OR value, update it
        if current_or > max_or:
            max_or = current_or
        
        # If we have used all our operations, break the loop
        if k == 0:
            break
        
        # Multiply the current number by x and add it to the list
        numbers[i] *= x
        k -= 1
    
    return max_or

def main():
    n, k, x = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(get_max_or(numbers, k, x))

if __name__ == '__main__':
    main()

