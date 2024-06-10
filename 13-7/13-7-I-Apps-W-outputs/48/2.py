
def buy_shares(n, s, r):
    # Initialize variables
    max_shares = 0
    total_cost = 0
    
    # Iterate through the opportunities to buy shares
    for i in range(n):
        # Calculate the number of shares that can be bought with the current opportunity
        shares = r // s[i]
        # Update the maximum number of shares that can be bought
        max_shares = max(max_shares, shares)
        # Update the total cost of buying the maximum number of shares
        total_cost += shares * s[i]
    
    # Return the maximum number of shares that can be bought and the total cost
    return max_shares, total_cost

def sell_shares(n, b, max_shares):
    # Initialize variables
    max_profit = 0
    total_profit = 0
    
    # Iterate through the opportunities to sell shares
    for i in range(n):
        # Calculate the number of shares that can be sold with the current opportunity
        shares = min(max_shares, b[i])
        # Update the maximum profit from selling the shares
        max_profit = max(max_profit, shares * b[i])
        # Update the total profit from selling the maximum number of shares
        total_profit += shares * b[i]
    
    # Return the maximum profit and the total profit
    return max_profit, total_profit

def solve(n, m, r, s, b):
    # Buy shares
    max_shares, total_cost = buy_shares(n, s, r)
    # Sell shares
    max_profit, total_profit = sell_shares(m, b, max_shares)
    # Return the maximum number of bourles that can be held after the evening
    return total_profit - total_cost

if __name__ == '__main__':
    n, m, r = map(int, input().split())
    s = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, m, r, s, b))

