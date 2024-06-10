
def get_possible_purchases(clients, colored_paintings, black_and_white_paintings, minimum_number_of_clients):
    # Initialize a set to store the possible purchases
    possible_purchases = set()
    
    # Loop through each client and add their preferences to the possible purchases
    for client in clients:
        for i in range(colored_paintings[client]):
            possible_purchases.add((client, i, 0))
        for j in range(black_and_white_paintings[client]):
            possible_purchases.add((client, 0, j))
    
    # Loop through each possible purchase and check if it satisfies the minimum number of clients requirement
    satisfied_purchases = []
    for purchase in possible_purchases:
        if purchase[0] in satisfied_purchases:
            continue
        if len([1 for client in clients if client == purchase[0] or (client in satisfied_purchases and (purchase[1] > 0 or purchase[2] > 0))]) >= minimum_number_of_clients:
            satisfied_purchases.append(purchase[0])
    
    # Return the number of satisfied purchases modulo 10007
    return len(satisfied_purchases) % 10007

def main():
    # Read the number of clients, colored paintings, black and white paintings, and the minimum number of clients from stdin
    num_clients, minimum_number_of_clients = map(int, input().split())
    colored_paintings = list(map(int, input().split()))
    black_and_white_paintings = list(map(int, input().split()))
    
    # Read the number of requirement changes from stdin
    num_requirement_changes = int(input())
    
    # Loop through each requirement change and print the number of possible purchases modulo 10007
    for _ in range(num_requirement_changes):
        client, colored_paintings[client], black_and_white_paintings[client] = map(int, input().split())
        print(get_possible_purchases(range(1, num_clients + 1), colored_paintings, black_and_white_paintings, minimum_number_of_clients))

if __name__ == '__main__':
    main()

