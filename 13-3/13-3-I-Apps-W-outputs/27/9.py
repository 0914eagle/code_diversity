
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
        contribution = contribution_1 + contribution_2
        # Add the contribution to the total contribution
        total_contribution += contribution
        # Increment the number of tickets sold
        num_tickets += 1
        # If the total contribution is greater than or equal to the required amount, break the loop
        if total_contribution >= k:
            break
    # Return the minimum number of tickets needed to reach the required total contribution
    return num_tickets

def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        prices = list(map(int, input().split()))
        x, a = map(int, input().split())
        y, b = map(int, input().split())
        k = int(input())
        print(get_min_tickets(prices, x, a, y, b, k))

if __name__ == '__main__':
    main()

