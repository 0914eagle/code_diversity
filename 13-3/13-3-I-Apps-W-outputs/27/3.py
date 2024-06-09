
def get_min_tickets(prices, x, a, y, b, k):
    # Sort the prices in non-decreasing order
    prices.sort()
    # Initialize the total contribution and the number of tickets sold
    total_contribution = 0
    num_tickets = 0
    # Loop through the prices and sell the tickets in the order they are sorted
    for price in prices:
        # Calculate the contribution from this ticket to the first program
        contribution_1 = price * x / 100
        # Calculate the contribution from this ticket to the second program
        contribution_2 = price * y / 100
        # Calculate the total contribution from this ticket
        total_contribution += contribution_1 + contribution_2
        # Increment the number of tickets sold
        num_tickets += 1
        # If the total contribution is greater than or equal to the required amount, return the number of tickets sold
        if total_contribution >= k:
            return num_tickets
    # If all the tickets are sold and the total contribution is less than the required amount, return -1
    return -1

def main():
    queries = int(input())
    for i in range(queries):
        n = int(input())
        prices = list(map(int, input().split()))
        x, a = map(int, input().split())
        y, b = map(int, input().split())
        k = int(input())
        print(get_min_tickets(prices, x, a, y, b, k))

if __name__ == '__main__':
    main()

