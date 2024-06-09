
def get_min_cost(numbers):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Iterate over all possible signs
    for sign in [-1, 1]:
        # Initialize the current cost to 0
        current_cost = 0
        
        # Iterate over all numbers
        for i, num in enumerate(numbers):
            # If the number is not equal to the sign, add the cost of changing it
            if num != sign:
                current_cost += 1
                
                # Update the number to the sign
                numbers[i] = sign
        
        # If the current cost is less than the minimum cost, update the minimum cost
        if current_cost < min_cost:
            min_cost = current_cost
    
    # Return the minimum cost
    return min_cost

def main():
    # Read the input
    n = int(input())
    numbers = list(map(int, input().split()))
    
    # Get the minimum cost
    min_cost = get_min_cost(numbers)
    
    # Print the minimum cost
    print(min_cost)

if __name__ == '__main__':
    main()

