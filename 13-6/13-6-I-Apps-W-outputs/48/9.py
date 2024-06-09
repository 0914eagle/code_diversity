
def get_min_cost(numbers):
    # Initialize the minimum cost to pay
    min_cost = 0
    # Initialize the product of the numbers
    product = 1
    # Iterate through the numbers
    for i in range(len(numbers)):
        # If the current number is not equal to 1, we need to pay a cost
        if numbers[i] != 1:
            # Calculate the cost to make the current number equal to 1
            cost = abs(numbers[i] - 1)
            # Add the cost to the minimum cost
            min_cost += cost
            # Update the product of the numbers
            product *= numbers[i]
    # Return the minimum cost
    return min_cost

def main():
    # Read the number of numbers and the numbers from stdin
    n = int(input())
    numbers = list(map(int, input().split()))
    # Get the minimum cost to make the product equal to 1
    min_cost = get_min_cost(numbers)
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

