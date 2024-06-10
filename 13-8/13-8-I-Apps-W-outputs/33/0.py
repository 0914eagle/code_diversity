
def get_input():
    n, c_1, c_2 = map(int, input().split())
    visitors = list(map(int, input()))
    return n, c_1, c_2, visitors

def solve(n, c_1, c_2, visitors):
    # Initialize the minimum price to infinity
    min_price = float('inf')
    
    # Iterate over all possible group sizes
    for group_size in range(1, n + 1):
        # Initialize the price for this group size to 0
        price = 0
        
        # Iterate over all possible combinations of visitors in the group
        for combination in itertools.combinations(visitors, group_size):
            # Calculate the price for this combination
            price_combination = c_1 + c_2 * (group_size - 1) ** 2
            
            # If the price for this combination is less than the minimum price, update the minimum price
            if price_combination < min_price:
                min_price = price_combination
        
        # Add the price for this group size to the total price
        price += min_price
    
    # Return the total price
    return price

def main():
    n, c_1, c_2, visitors = get_input()
    print(solve(n, c_1, c_2, visitors))

if __name__ == '__main__':
    main()

