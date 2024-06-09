
def get_min_cost(numbers):
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Initialize the minimum cost to 0
    min_cost = 0
    # Loop through the numbers
    for i in range(len(numbers)):
        # Calculate the cost of transforming the current number into the median of the sorted numbers
        cost = (numbers[i] - numbers[len(numbers)//2])**2
        # Add the cost to the minimum cost
        min_cost += cost
    # Return the minimum cost
    return min_cost

def main():
    # Read the number of integers and the integers from stdin
    n = int(input())
    numbers = list(map(int, input().split()))
    # Get the minimum cost to achieve Evi's objective
    min_cost = get_min_cost(numbers)
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

