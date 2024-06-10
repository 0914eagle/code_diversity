
def get_largest_divisible_number(cards):
    # Initialize a list to store the numbers
    numbers = []
    
    # Iterate through the cards and append the numbers to the list
    for card in cards:
        if card == 0:
            numbers.append(0)
        else:
            numbers.append(5)
    
    # Sort the numbers in descending order
    numbers.sort(reverse=True)
    
    # Initialize a variable to store the largest number divisible by 90
    largest_divisible_number = 0
    
    # Iterate through the numbers and check if they are divisible by 90
    for number in numbers:
        if number % 9 == 0:
            largest_divisible_number = number
            break
    
    # Return the largest number divisible by 90
    return largest_divisible_number

def main():
    # Read the input from stdin
    n = int(input())
    cards = list(map(int, input().split()))
    
    # Call the function to get the largest number divisible by 90
    largest_divisible_number = get_largest_divisible_number(cards)
    
    # Print the output
    print(largest_divisible_number)

if __name__ == '__main__':
    main()

