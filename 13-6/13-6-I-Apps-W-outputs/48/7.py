
def get_min_cost(numbers):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    
    # Iterate over all possible combinations of signs
    for signs in itertools.product([1, -1], repeat=len(numbers)):
        # Calculate the product of the numbers with the current signs
        product = 1
        for i in range(len(numbers)):
            product *= numbers[i] * signs[i]
        
        # If the product is equal to 1, return the current cost
        if product == 1:
            return len(numbers) - sum(signs)
        
        # If the product is not equal to 1, calculate the cost of changing the signs
        cost = 0
        for i in range(len(numbers)):
            if signs[i] != 1:
                cost += abs(numbers[i])
        
        # Update the minimum cost if the current cost is lower
        if cost < min_cost:
            min_cost = cost
    
    # Return the minimum cost
    return min_cost

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(get_min_cost(numbers))

if __name__ == '__main__':
    main()

