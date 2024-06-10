
def get_number_of_different_purchases(clients, min_colored_paintings):
    
    # Initialize a set to store the purchases
    purchases = set()
    
    # Iterate over the clients
    for client in clients:
        # Get the maximum number of colored paintings and black and white paintings that the client wants
        max_colored_paintings, max_black_and_white_paintings = client
        
        # Iterate over the number of colored paintings that the client wants
        for colored_paintings in range(1, max_colored_paintings + 1):
            # Get the number of black and white paintings that the client wants
            black_and_white_paintings = max_colored_paintings - colored_paintings
            
            # If the client wants at least the minimum number of colored paintings, add the purchase to the set
            if colored_paintings >= min_colored_paintings:
                purchases.add((colored_paintings, black_and_white_paintings))
    
    # Return the number of different purchases
    return len(purchases)

def main():
    # Read the input
    num_clients, min_colored_paintings = map(int, input().split())
    clients = [list(map(int, input().split())) for _ in range(num_clients)]
    num_requirement_changes = int(input())
    requirement_changes = [list(map(int, input().split())) for _ in range(num_requirement_changes)]
    
    # Initialize the output
    output = []
    
    # Iterate over the requirement changes
    for client, max_colored_paintings, max_black_and_white_paintings in requirement_changes:
        # Get the number of different purchases
        number_of_different_purchases = get_number_of_different_purchases(clients, min_colored_paintings)
        
        # Add the number of different purchases to the output
        output.append(number_of_different_purchases)
    
    # Print the output
    for number_of_different_purchases in output:
        print(number_of_different_purchases % 10000)

if __name__ == '__main__':
    main()

